import streamlit as st
from .create_user_profile import create_user_profile
from .get_user_profile import get_user_profile
import streamlit as st
from objects.util.page import page_group
import components
from router.routes import get_routes

def header():
    with st.container():
        left, right = st.columns([0.6, 0.4], vertical_alignment= "center")
        with right:
            if not st.user.is_logged_in:
                if st.button("Log in"):
                    st.login("google")
            else:
                if st.button("Log out"):
                    st.logout()
                # retrieve user profile after success login
                user_profile = get_user_profile()
                
                # if no profile make a basic one with st.user data
                if not user_profile:
                    user_profile = create_user_profile()

                #store profile in session state
                st.session_state["user_profile"] = user_profile
                with left:
                    if st.user.is_logged_in:
                        pp_left, text_right = st.columns([0.4, 0.6])
                        with pp_left:
                            st.image(st.user.picture, width=50)
                        with text_right:
                            if "user_profile" in st.session_state and "givenname" in st.session_state["user_profile"]:
                                st.markdown(f"`{st.session_state["user_profile"]["givenname"]}`")

def navigation():
    routes = get_routes()
    page = page_group("p")

    general_routes = {}
    user_routes = {}
    admin_routes = {}

    with st.sidebar:
        header()
        st.title("TMM Legacy League")

        current_roles = get_current_roles()

        for label, meta in routes.items():
            roles = meta["roles"]
            if not is_allowed(roles, current_roles):
                continue

            if roles is None:
                general_routes[label] = meta
            elif "user" in roles:
                user_routes[label] = meta
            elif roles == ["admin"]:
                admin_routes[label] = meta
            else:
                general_routes[label] = meta

        default_already_set = [False]  # Using list for mutability in nested scope

        if general_routes:
            add_routes_to_expander(page, "GENERAL", general_routes, default_already_set)
        if user_routes:
            add_routes_to_expander(page, "USER", user_routes, default_already_set)
        if admin_routes:
            add_routes_to_expander(page, "ADMIN", admin_routes, default_already_set)

    page.show()

def is_allowed(allowed_roles, current_roles):
    if allowed_roles is None:
        return True
    # Check if any user role is in allowed_roles
    return any(role in allowed_roles for role in current_roles)

def add_routes_to_expander(page, title, routes_dict, default_already_set):
    with st.expander(title, True):
        for label, meta in routes_dict.items():
            component_func = getattr(components, meta["component"])
            # Set default only if not set yet
            if not default_already_set[0]:
                page.item(label, component_func, default=True)
                default_already_set[0] = True
            else:
                page.item(label, component_func, default=False)

def get_current_roles():
    # Try to get roles from session state user_profile, fallback to empty list
    profile = st.session_state.get("user_profile", {})
    return profile.get("roles", []) if profile else []