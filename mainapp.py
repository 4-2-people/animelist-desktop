import os
import tkinter
import customtkinter
import requests
from PIL import Image

customtkinter.set_appearance_mode("dark")
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bg_img/test img")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("AnimeList")
        self.geometry("700x450")
        self.iconphoto(False, tkinter.PhotoImage(file="bg_img/test img/app_logo.png"))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation_frame = NavigationFrame(self)
        self.frame_home = HomeFrame(self)
        self.frame_registration = RegistrationFrame(self)
        self.frame_login = LoginFrame(self)
        self.frame_profile = ProfileFrame(self)

        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.frame_home.grid(row=0, column=1, sticky="nsew")

    def show_frame_by_name(self, name: str):
        if name == "home":
            self.frame_home.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_home.grid_forget()
        if name == "frame_registration":
            self.frame_registration.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_registration.grid_forget()
        if name == "frame_login":
            self.frame_login.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_login.grid_forget()
        if name == "frame_profile":
            self.frame_profile.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_profile.grid_forget()

    def unlock_navigation_bar(self):
        self.navigation_frame.unlock_navigation_bar()


class NavigationFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.logo_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "user_avatar_light.png")),
            dark_image=Image.open(os.path.join(image_path, "user_avatar_dark.png")),
            size=(26, 26)
        )
        self.home_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "home_light.png")),
            dark_image=Image.open(os.path.join(image_path, "home_dark.png")),
            size=(20, 20)
        )
        self.chat_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "chat_light.png")),
            dark_image=Image.open(os.path.join(image_path, "chat_dark.png")),
            size=(20, 20)
        )
        self.profile_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "profile_light.png")),
            dark_image=Image.open(os.path.join(image_path, "profile_dark.png")),
            size=(20, 20)
        )
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "add_user_light.png")),
            dark_image=Image.open(os.path.join(image_path, "add_user_dark.png")), size=(20, 20)
        )
        self.user_login_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "user_login_light.png")),
            dark_image=Image.open(os.path.join(image_path, "user_login_dark.png")), size=(20, 20)
        )
        self.user_registration_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "user_registration_light.png")),
            dark_image=Image.open(os.path.join(image_path, "user_registration_dark.png")), size=(20, 20)
        )
        self.found_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "search_light.png")),
            dark_image=Image.open(os.path.join(image_path, "search_dark.png")),
            size=(20, 20)
        )
        self.hide_navbar_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "hidebar_light.png")),
            dark_image=Image.open(os.path.join(image_path, "hidebar_dark.png")),
            size=(20, 20)
        )
        self.show_navbar_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "show_light.png")),
            dark_image=Image.open(os.path.join(image_path, "show_dark.png")),
            size=(20, 20)
        )
        self.navigation_frame_label = customtkinter.CTkLabel(
            self, text="  Anonymous guest",
            image=self.logo_image,
            compound="left",
            font=customtkinter.CTkFont(size=15, weight="bold")
        )
        self.navigation_home_button = customtkinter.CTkButton(
            self, corner_radius=0, height=40, border_spacing=10,
            text="Home",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.home_image,
            anchor="w",
            command=lambda: self.select_frame_by_name("frame_home")
        )
        self.navigation_registration_button = customtkinter.CTkButton(
            self, corner_radius=0, height=40, border_spacing=10,
            text="Registration",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.user_registration_image,
            anchor="w",
            command=lambda: self.select_frame_by_name("frame_registration")
        )
        self.navigation_login_button = customtkinter.CTkButton(
            self, corner_radius=0, height=40, border_spacing=10,
            text="Login",
            fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.user_login_image,
            anchor="w",
            command=lambda: self.select_frame_by_name("frame_login")
        )
        self.navigation_profile_button = customtkinter.CTkButton(
            self, corner_radius=0, height=40, border_spacing=10,
            text="Profile",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.profile_image,
            anchor="w",
            command=lambda: self.select_frame_by_name("frame_profile")
        )
        self.navigation_chat_button = customtkinter.CTkButton(
            self, corner_radius=0, height=40, border_spacing=10,
            text="Chat",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.chat_image,
            anchor="w",
            state='disabled',
            command=lambda: self.select_frame_by_name("frame_chat")
        )
        self.navigation_add_friend_button = customtkinter.CTkButton(
            self, corner_radius=0, height=40, border_spacing=10,
            text="Add friend",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.add_user_image,
            anchor="w",
            state='disabled',
            command=lambda: self.select_frame_by_name("frame_add_friend")
        )
        self.navigation_found_button = customtkinter.CTkButton(
            self, corner_radius=0, height=40,
            border_spacing=10, text="Found anime",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.found_image,
            anchor="w",
            state='disabled',
            command=lambda: self.select_frame_by_name("frame_found")
        )
        self.navigation_appearance_mode_menu = customtkinter.CTkOptionMenu(
            self, values=["Light", "Dark", "System"],
            command=lambda mode: customtkinter.set_appearance_mode(mode)
        )

        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
        self.navigation_home_button.grid(row=1, column=0, sticky="ew")
        self.navigation_registration_button.grid(row=2, column=0, sticky="ew")
        self.navigation_login_button.grid(row=3, column=0, sticky="ew")
        self.navigation_appearance_mode_menu.grid(row=8, column=0, padx=20, pady=20, sticky="s")

    def select_frame_by_name(self, name: str):
        self.navigation_home_button.configure(fg_color=("gray75", "gray25") if name == "frame_home" else "transparent")
        self.navigation_registration_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_registration" else "transparent")
        self.navigation_login_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_login" else "transparent")
        self.navigation_profile_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_profile" else "transparent")
        self.navigation_add_friend_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_add_friend" else "transparent")
        self.navigation_found_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_found" else "transparent")

        self.master.show_frame_by_name(name)

    def unlock_navigation_bar(self):
        self.navigation_profile_button.grid(row=2, column=0, sticky="ew")
        self.navigation_chat_button.grid(row=3, column=0, sticky="ew")
        self.navigation_add_friend_button.grid(row=4, column=0, sticky="ew")
        self.navigation_found_button.grid(row=5, column=0, sticky="ew")


class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.corner_radius = 0
        self.fg_color = "transparent"
        self.grid_columnconfigure(0, weight=1)

        self.large_test_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "large_img.jpg")), size=(500, 150)
        )
        self.icon_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "app_logo.png")), size=(20, 20)
        )
        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self, text="", image=self.large_test_image
        )
        self.home_frame_button_1 = customtkinter.CTkButton(self, text="", image=self.icon_image)

        self.home_frame_button_2 = customtkinter.CTkButton(
            self, text="CTkButton", image=self.icon_image, compound="right"
        )
        self.home_frame_button_3 = customtkinter.CTkButton(
            self, text="CTkButton", image=self.icon_image, compound="top"
        )
        self.home_frame_button_4 = customtkinter.CTkButton(
            self, text="CTkButton", image=self.icon_image, compound="bottom", anchor="w"
        )

        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)


class RegistrationFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.corner_radius = 0
        self.fg_color = "transparent"
        self.grid_columnconfigure(0, weight=1)

        self.registration_label = customtkinter.CTkLabel(
            self, text="Animelist\nRegistration Page", font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.registration_username_entry = customtkinter.CTkEntry(
            self, width=200, placeholder_text="username"
        )
        self.registration_email_entry = customtkinter.CTkEntry(
            self, width=200, placeholder_text="email"
        )
        self.registration_password_entry = customtkinter.CTkEntry(
            self, width=200, show="*", placeholder_text="enter password"
        )
        self.registration_password_repeat_entry = customtkinter.CTkEntry(
            self, width=200, show="*", placeholder_text="repeat password"
        )
        self.registration_button = customtkinter.CTkButton(
            self, text="register", command=self.registration_event, width=200
        )
        self.registration_label_error = customtkinter.CTkLabel(
            self, text="", text_color='red', font=customtkinter.CTkFont(size=14, weight="bold")
        )

        self.registration_label.grid(row=0, column=0, padx=30, pady=(40, 15))
        self.registration_username_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.registration_email_entry.grid(row=3, column=0, padx=30, pady=(0, 15))
        self.registration_password_entry.grid(row=4, column=0, padx=30, pady=(0, 15))
        self.registration_password_repeat_entry.grid(row=5, column=0, padx=30, pady=(0, 15))
        self.registration_button.grid(row=6, column=0, padx=30, pady=(15, 15))
        self.registration_label_error.grid(row=7, column=0, padx=30, pady=(15, 15))

    def registration_event(self):
        self.registration_label_error.configure(text="")
        username = self.registration_username_entry.get()
        email = self.registration_email_entry.get()
        if self.registration_password_entry.get() != self.registration_password_repeat_entry.get():
            self.registration_label_error.configure(text="пароли не совпадают")
        else:
            password = self.registration_password_entry.get()
            response = requests.post(
                'http://localhost:8000/v1/auth/sign-up',
                json={"username": username, "email": email, "password": password}
            )
            data = response.json()
            response_text = data.get("detail", "Сервер пал")
            self.registration_label_error.configure(text=response_text)
            if response.status_code == requests.codes.created:
                self.master.show_frame_by_name("frame_login")


class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.corner_radius = 0
        self.fg_color = "transparent"
        self.grid_columnconfigure(0, weight=1)

        self.login_label = customtkinter.CTkLabel(
            self, text="Animelist\nLogin Page", font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.login_username_entry = customtkinter.CTkEntry(self, width=200, placeholder_text="username")
        self.login_password_entry = customtkinter.CTkEntry(
            self, width=200, show="*", placeholder_text="password"
        )
        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.login_event, width=200)
        self.login_label_error = customtkinter.CTkLabel(
            self, text="", text_color='red', font=customtkinter.CTkFont(size=14, weight="bold")
        )

        self.login_label.grid(row=1, column=0, padx=30, pady=(40, 15))
        self.login_username_entry.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.login_password_entry.grid(row=3, column=0, padx=30, pady=(0, 15))
        self.login_button.grid(row=4, column=0, padx=30, pady=(15, 15))
        self.login_label_error.grid(row=5, column=0, padx=30, pady=(15, 15))

    def login_event(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()
        try:
            answer = requests.get('http://localhost:8000/v1/auth/current', auth=(username, password))
            response = answer.json()
        except:
            self.login_label_error.configure(text="Сервер не отвечает")
        if 'answer' in locals() and answer.status_code == requests.codes.ok:
            self.master.unlock_navigation_bar()
        if 'response' in locals():
            self.login_label_error.configure(text=response.get("detail", "Сервер пал"))
            # self.navigation_frame_label.configure(text=response['username'])
            # self.profile_username_label.configure(text=response['username'])
            # self.profile_email_label.configure(text=response['email'])
            # self.master.show_frame_by_name("frame_profile")


class ProfileFrame(customtkinter.CTkFrame):
    corner_radius = 0
    fg_color = "transparent"

    def __init__(self, parent):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)

        self.profile_label = customtkinter.CTkLabel(
            self, text="Animelist\nProfile Page", font=customtkinter.CTkFont(size=20, weight="bold")
        )
        customtkinter.CTkLabel(self, text="username: ").grid(row=2, column=0, sticky="e")
        customtkinter.CTkLabel(self, text="email: ").grid(row=3, column=0, sticky="e")
        self.profile_username_label = customtkinter.CTkLabel(self, text="")
        self.profile_email_label = customtkinter.CTkLabel(self, text="")

        self.profile_label.grid(row=1, column=0, padx=15, pady=(20, 15))
        self.profile_username_label.grid(row=2, column=1, sticky="w")
        self.profile_email_label.grid(row=3, column=1, sticky="w")


if __name__ == "__main__":
    App().mainloop()
