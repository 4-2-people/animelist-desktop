import customtkinter
import tkinter
import requests
import json
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("AnimeList")
        self.geometry("700x450")
        self.iconphoto(False, tkinter.PhotoImage(file="bg_img/test img/app_logo.png"))

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bg_img/test img")
        self.logo_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "user_avatar_light.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "user_avatar_dark.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_img.jpg")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "app_logo.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_light.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_dark.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_light.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_dark.png")), size=(20, 20))
        self.profile_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "profile_light.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "profile_dark.png")),
                                                 size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_dark.png")), size=(20, 20))
        self.user_login_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "user_login_light.png")),
            dark_image=Image.open(os.path.join(image_path, "user_login_dark.png")), size=(20, 20))
        self.user_registration_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "user_registration_light.png")),
            dark_image=Image.open(os.path.join(image_path, "user_registration_dark.png")), size=(20, 20))
        self.found_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "search_light.png")),
                                                  dark_image=Image.open(os.path.join(image_path, "search_dark.png")),
                                                  size=(20, 20))
        self.hide_navbar_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "hidebar_light.png")),
            dark_image=Image.open(os.path.join(image_path, "hidebar_dark.png")), size=(20, 20))
        self.show_navbar_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "show_light.png")),
            dark_image=Image.open(os.path.join(image_path, "show_dark.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=0)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Anonymous guest", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.nav_registration_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                               border_spacing=10, text="Registration",
                                                               fg_color="transparent", text_color=("gray10", "gray90"),
                                                               hover_color=("gray70", "gray30"),
                                                               image=self.user_registration_image, anchor="w",
                                                               command=self.frame_registration_button_event)
        self.nav_registration_button.grid(row=2, column=0, sticky="ew")

        self.nav_login_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                          border_spacing=10, text="Login",
                                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          image=self.user_login_image, anchor="w",
                                                          command=self.frame_login_button_event)
        self.nav_login_button.grid(row=3, column=0, sticky="ew")

        self.nav_profile_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                        border_spacing=10, text="Profile",
                                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),
                                                        image=self.profile_image, anchor="w",
                                                        command=self.frame_profile_button_event)

        self.frame_chat_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Chat",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", state='disabled', command=self.frame_chat_button_event)
        #

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Add friend",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", state='disabled', command=self.frame_3_button_event)
        #

        self.frame_found_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Found anime",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.found_image, anchor="w", state='disabled',
                                                      command=self.frame_found_button_event)
        #

        self.hide_navbar_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="<<",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.hide_navbar_image, anchor="w",
                                                      command=self.hide_bar_button_event)
        self.hide_navbar_button.grid(row=7, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=8, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create registration frame
        self.frame_registration = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_registration.grid_columnconfigure(0, weight=1)

        self.registration_label = customtkinter.CTkLabel(self.frame_registration, text="Animelist\nRegistration Page",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.registration_label.grid(row=0, column=0, padx=30, pady=(40, 15))
        self.registration_username_entry = customtkinter.CTkEntry(self.frame_registration, width=200, placeholder_text="username")
        self.registration_username_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.registration_email_entry = customtkinter.CTkEntry(self.frame_registration, width=200,
                                                                  placeholder_text="email")
        self.registration_email_entry.grid(row=3, column=0, padx=30, pady=(0, 15))
        self.registration_password_entry = customtkinter.CTkEntry(self.frame_registration, width=200, show="*", placeholder_text="enter password")
        self.registration_password_entry.grid(row=4, column=0, padx=30, pady=(0, 15))
        self.registration_password_repeat_entry = customtkinter.CTkEntry(self.frame_registration, width=200, show="*",
                                                                  placeholder_text="repeat password")
        self.registration_password_repeat_entry.grid(row=5, column=0, padx=30, pady=(0, 15))
        self.registration_button = customtkinter.CTkButton(self.frame_registration, text="register", command=self.registration_event, width=200)
        self.registration_button.grid(row=6, column=0, padx=30, pady=(15, 15))
        self.registration_label_error = customtkinter.CTkLabel(self.frame_registration, text="", text_color='red',
                                                  font=customtkinter.CTkFont(size=14, weight="bold"))
        self.registration_label_error.grid(row=7, column=0, padx=30, pady=(15, 15))

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/bg_img/pink theme/sakura_pink.jpg"),
                                               size=(450, 450))
        self.bg_image_label = customtkinter.CTkLabel(self.frame_registration, text='', image=self.bg_image)
        self.bg_image_label.grid()

        # create login frame
        self.frame_login = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_login.grid_columnconfigure(0, weight=1)

        # load and create background image
        # current_path = os.path.dirname(os.path.realpath(__file__))
        # self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/bg_img/pink theme/sakura_pink.jpg"),
        #                                        size=(450, 450))
        # self.bg_image_label = customtkinter.CTkLabel(self.frame_login, image=self.bg_image)
        # self.bg_image_label.grid(row=0, column=0)

        self.login_label = customtkinter.CTkLabel(self.frame_login, text="Animelist\nLogin Page",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=1, column=0, padx=30, pady=(40, 15))
        self.login_username_entry = customtkinter.CTkEntry(self.frame_login, width=200, placeholder_text="username")
        self.login_username_entry.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.login_password_entry = customtkinter.CTkEntry(self.frame_login, width=200, show="*", placeholder_text="password")
        self.login_password_entry.grid(row=3, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.frame_login, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=4, column=0, padx=30, pady=(15, 15))
        self.login_label_error = customtkinter.CTkLabel(self.frame_login, text="", text_color='red',
                                                        font=customtkinter.CTkFont(size=14, weight="bold"))
        self.login_label_error.grid(row=5, column=0, padx=30, pady=(15, 15))

        # create profile frame
        self.frame_profile = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_profile.grid_columnconfigure(0, weight=1)

        self.profile_label = customtkinter.CTkLabel(self.frame_profile, text="Animelist\nProfile Page",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.profile_label.grid(row=1, column=0, padx=15, pady=(20, 15))
        customtkinter.CTkLabel(self.frame_profile, text="username: ").grid(row=2, column=0, sticky="e")
        customtkinter.CTkLabel(self.frame_profile, text="email: ").grid(row=3, column=0, sticky="e")
        self.profile_username_label = customtkinter.CTkLabel(self.frame_profile, text="")
        self.profile_username_label.grid(row=2, column=1, sticky="w")
        self.profile_email_label = customtkinter.CTkLabel(self.frame_profile, text="")
        self.profile_email_label.grid(row=3, column=1, sticky="w")



        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create found frame
        self.found_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        customtkinter.CTkLabel(self.found_frame, text="Поиск по названию").grid(row=0, column=0, padx=10, pady=10)
        self.input_for_found = customtkinter.CTkEntry(self.found_frame)
        self.input_for_found.grid(row=0, column=1, padx=10, pady=10)
        self.found_button = customtkinter.CTkButton(self.found_frame, text='', image=self.found_image, command=self.found_anime)
        self.found_button.grid(row=0, column=2, padx=10, pady=10)
        customtkinter.CTkLabel(self.found_frame, text='img').grid(row=1, column=0, padx=10, pady=10)
        customtkinter.CTkLabel(self.found_frame, text='title').grid(row=1, column=1, padx=10, pady=10)
        customtkinter.CTkLabel(self.found_frame, text='raiting').grid(row=1, column=2, padx=10, pady=10)
        self.founded_anime_img = customtkinter.CTkLabel(self.found_frame, text='')
        self.founded_anime_img.grid(row=2, column=0, padx=10, pady=10)
        self.founded_anime_title = customtkinter.CTkLabel(self.found_frame, text='')
        self.founded_anime_title.grid(row=2, column=1, padx=10, pady=10)
        self.founded_anime_raiting = customtkinter.CTkLabel(self.found_frame, text='')
        self.founded_anime_raiting.grid(row=2, column=2, padx=10, pady=10)


        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name: str):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.nav_registration_button.configure(fg_color=("gray75", "gray25") if name == "frame_registration" else "transparent")
        self.nav_login_button.configure(fg_color=("gray75", "gray25") if name == "frame_login" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_found_button.configure(fg_color=("gray75", "gray25") if name == "frame_found" else "transparent")
        self.nav_profile_button.configure(fg_color=("gray75", "gray25") if name == "frame_profile" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
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
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_found":
            self.found_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.found_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_registration_button_event(self):
        self.select_frame_by_name("frame_registration")

    def frame_login_button_event(self):
        self.select_frame_by_name("frame_login")

    def frame_profile_button_event(self):
        self.select_frame_by_name("frame_profile")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_found_button_event(self):
        self.select_frame_by_name("frame_found")

    def found_anime(self):
        pass

    def hide_bar_button_event(self):
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=0)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_login_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w",
                                                      command=self.frame_login_button_event)
        self.frame_login_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_found_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                          border_spacing=10, text="",
                                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          image=self.found_image, anchor="w",
                                                          command=self.frame_found_button_event)
        self.frame_found_button.grid(row=4, column=0, sticky="ew")

        self.hide_navbar_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                          border_spacing=10, text="",
                                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          image=self.show_navbar_image, anchor="w",
                                                          command=self.hide_bar_button_event)
        self.hide_navbar_button.grid(row=7, column=0, sticky="ew")

        # self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
        #                                                         values=["Light", "Dark", "System"],
        #                                                         command=self.change_appearance_mode_event)
        # self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def registration_event(self):
        self.registration_label_error.configure(text="")
        username = self.registration_username_entry.get()
        email = self.registration_email_entry.get()
        if self.registration_password_entry.get() != self.registration_password_repeat_entry.get():
            self.registration_label_error.configure(text="пароли не совпадают")

        else:
            password = self.registration_password_entry.get()
            answer = requests.post('http://localhost:8000/v1/auth/sign-up', json={"username": username, "email": email, "password": password})
            response = answer.json()
            response_text = response['detail']
            self.registration_label_error.configure(text=f"{response_text}")
            if answer.status_code < 400:
                self.select_frame_by_name("frame_login")
                self.login_username_entry.insert(0, username)
                self.login_password_entry.insert(0, password)


    def login_event(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()
        answer = requests.get('http://localhost:8000/v1/auth/current', auth=(username, password))
        response = answer.json()
        if answer.status_code < 400:
            self.nav_profile_button.grid(row=2, column=0, sticky="ew")
            self.frame_chat_button.grid(row=3, column=0, sticky="ew")
            self.frame_3_button.grid(row=4, column=0, sticky="ew")
            self.frame_found_button.grid(row=5, column=0, sticky="ew")
            self.navigation_frame_label.configure(text=response['username'])
            self.profile_username_label.configure(text=response['username'])
            self.profile_email_label.configure(text=response['email'])
            self.select_frame_by_name("frame_profile")
        else:
            self.login_label_error.configure(text=response["detail"])


    def frame_chat_button_event(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()