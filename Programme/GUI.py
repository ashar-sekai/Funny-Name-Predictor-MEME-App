import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk
import os

# App colors and font palette
BG_COLOR = "#1e1e2f"
FG_COLOR = "#ffffff"
ACCENT_COLOR = "#4f46e5"
FONT_TITLE = ("Segoe UI", 24, "bold")
FONT_SUB = ("Segoe UI", 16)
FONT_BUTTON = ("Segoe UI", 12, "bold")
FONT_LOADING = ("Consolas", 16)
FONT_HELLO = ("Segoe UI", 32, "bold")
PLACEHOLDER_COLOR = "#888888"  # New color for placeholder text

loading_messages = [
    "Evaluating Answer...",
    "Integrating AI models...",
    "Analyzing most efficient Quantum state for qubits using Grover's algorithm...",
    "Taking a break now dawg...",
    "Implementing Topological Entanglement...",
    "Ts is so peak...",
    "Alright, I'm done!"
]

class NamePredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Name Predictor App")
        self.root.configure(bg=BG_COLOR)
        self.root.geometry("1000x800")
        self.root.minsize(800, 600)
        
        self.center_window()
        self.explosion_gif = None
        self.fire_gif = None
        self.thumbs_img = None
        self.explosion_frames = []
        self.fire_frames = []
        self.load_gifs()
        
        self.container = tk.Frame(self.root, bg=BG_COLOR)
        self.container.pack(expand=True, fill=tk.BOTH)
        
        self.title_label = tk.Label(self.container, text="NAME PREDICTOR ULTRA JsadKAdlAKL'asdl;", 
                                  font=FONT_TITLE, bg=BG_COLOR, fg=ACCENT_COLOR)
        self.title_label.pack(pady=10)
        
        self.content_frame = tk.Frame(self.container, bg=BG_COLOR)
        self.content_frame.pack(expand=True, fill=tk.BOTH)
        
        self.thumbs_label = tk.Label(self.content_frame, bg=BG_COLOR)
        self.thumbs_label.pack(expand=True, fill=tk.BOTH)
        
        try:
            thumbs_path = r"C:\users\alias\documents\Year Predictor\Programme\thumbs.jpg"
            if os.path.exists(thumbs_path):
                self.thumbs_img = Image.open(thumbs_path)
                max_width = 900
                max_height = 600
                self.thumbs_img.thumbnail((max_width, max_height), Image.LANCZOS)
                self.thumbs_photo = ImageTk.PhotoImage(self.thumbs_img)
                self.thumbs_label.config(image=self.thumbs_photo)
        except Exception as e:
            print(f"Error loading thumbs.jpg: {e}")
        
        self.create_input_ui()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')
    
    def load_gifs(self):
        try:
            explosion_path = r"C:\users\alias\documents\Year Predictor\Programme\explosion.gif"
            if os.path.exists(explosion_path):
                self.explosion_gif = Image.open(explosion_path)
                for frame in range(self.explosion_gif.n_frames):
                    self.explosion_gif.seek(frame)
                    self.explosion_frames.append(ImageTk.PhotoImage(self.explosion_gif.copy()))
            
            fire_path = r"C:\users\alias\documents\Year Predictor\Programme\fire-california.gif"
            if os.path.exists(fire_path):
                self.fire_gif = Image.open(fire_path)
                for frame in range(self.fire_gif.n_frames):
                    self.fire_gif.seek(frame)
                    self.fire_frames.append(ImageTk.PhotoImage(self.fire_gif.copy()))
        except Exception as e:
            print(f"Error loading GIFs: {e}")

    def create_input_ui(self):
        self.clear_content_frame()

        if hasattr(self, 'thumbs_img') and self.thumbs_img:
            self.thumbs_label = tk.Label(self.content_frame, bg=BG_COLOR)
            self.thumbs_label.pack(expand=True, fill=tk.BOTH)
            self.thumbs_photo = ImageTk.PhotoImage(self.thumbs_img)
            self.thumbs_label.config(image=self.thumbs_photo)

        input_container = tk.Frame(self.content_frame, bg=BG_COLOR)
        input_container.pack(pady=20)

        self.subtitle_label = tk.Label(input_container, 
                                     text="I will predict your name with a 99.99% accuracy", 
                                     font=FONT_SUB, bg=BG_COLOR, fg=FG_COLOR)
        self.subtitle_label.pack(pady=(20, 10))

        input_frame = tk.Frame(input_container, bg=BG_COLOR)
        input_frame.pack()

        # Create entry box with proper placeholder implementation
        self.name_entry = tk.Entry(input_frame, font=FONT_SUB, width=30, 
                                 bg="#2e2e3e", fg=PLACEHOLDER_COLOR, insertbackground=FG_COLOR)
        self.name_entry.insert(0, "Enter your name here bhai")
        self.name_entry.bind("<FocusIn>", self.on_entry_click)
        self.name_entry.bind("<FocusOut>", self.on_focusout)
        self.name_entry.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.predict_button = tk.Button(input_frame, text="PREDICT NOW!", font=FONT_BUTTON, 
                                      bg=ACCENT_COLOR, fg=FG_COLOR, activebackground="#4338ca",
                                      command=self.start_loading)
        self.predict_button.pack(side=tk.LEFT, padx=10)

    def on_entry_click(self, event):
        """Function that gets called when entry is clicked"""
        if self.name_entry.get() == "Enter your name here bhai":
            self.name_entry.delete(0, tk.END)
            self.name_entry.config(fg=FG_COLOR)

    def on_focusout(self, event):
        """Function that gets called when entry loses focus"""
        if not self.name_entry.get():
            self.name_entry.insert(0, "Enter your name here bhai")
            self.name_entry.config(fg=PLACEHOLDER_COLOR)

    def start_loading(self):
        if hasattr(self, 'thumbs_label'):
            self.thumbs_label.pack_forget()
        
        self.name = self.name_entry.get().strip()
        if not self.name or self.name == "Enter your name here bhai":
            return

        self.clear_content_frame()
        
        loading_container = tk.Frame(self.content_frame, bg=BG_COLOR)
        loading_container.pack(expand=True, pady=40)
        
        self.loading_label = tk.Label(loading_container, text="", font=FONT_LOADING, 
                                    bg=BG_COLOR, fg=FG_COLOR)
        self.loading_label.pack(pady=20)

        self.progress = ttk.Progressbar(loading_container, mode="indeterminate", length=400)
        self.progress.pack(pady=10)
        self.progress.start()

        self.msg_index = 0
        self.show_loading_messages()

    def show_loading_messages(self):
        if self.msg_index >= len(loading_messages):
            self.progress.stop()
            self.clear_content_frame()
            self.show_result_ui()
            return

        msg = loading_messages[self.msg_index]
        self.loading_label.config(text=msg)

        delay = 5000 if msg == "Taking a break now dawg..." else random.randint(1000, 2000)
        self.msg_index += 1
        self.root.after(delay, self.show_loading_messages)

    def show_result_ui(self):
        result_frame = tk.Frame(self.content_frame, bg=BG_COLOR)
        result_frame.pack(expand=True, pady=40)
        
        tk.Label(result_frame, text="I predicted your name with a 99.99% accuracy, enjoy man!", 
                font=FONT_SUB, bg=BG_COLOR, fg=ACCENT_COLOR).pack(pady=20)

        self.reveal_frame = tk.Frame(result_frame, bg=BG_COLOR)
        self.reveal_frame.pack(pady=20)
        
        self.reveal_button = tk.Button(self.reveal_frame, text="Click to reveal", 
                                     font=FONT_BUTTON, bg=ACCENT_COLOR, fg=FG_COLOR,
                                     command=self.reveal_name)
        self.reveal_button.pack()

        # Prepare canvas for GIF chaos
        self.gif_canvas = tk.Canvas(self.content_frame, width=1000, height=600, 
                                   bg=BG_COLOR, highlightthickness=0)
        self.gif_canvas.pack_forget()
        self.gif_active = False

    def reveal_name(self):
        # Remove the button and replace with "hello world"
        self.reveal_button.destroy()
        
        self.hello_label = tk.Label(self.reveal_frame, text="", font=FONT_HELLO, 
                                  bg=BG_COLOR, fg=BG_COLOR)
        self.hello_label.pack()
        
        self.fade_opacity = 0
        self.fade_in_text()

    def fade_in_text(self):
        self.fade_opacity += 0.025  # 4 seconds total (1/40 per frame)
        if self.fade_opacity <= 1.0:
            faded_color = self.fade_color(FG_COLOR, BG_COLOR, self.fade_opacity)
            self.hello_label.config(text="hello world 🗿", fg=faded_color)
            self.root.after(100, self.fade_in_text)
        else:
            self.unleash_gif_chaos()
    
    def unleash_gif_chaos(self):
        self.gif_canvas.pack(fill=tk.BOTH, expand=True)
        self.gif_active = True
        
        # Create multiple GIF instances all over the screen
        self.gif_instances = []
        
        # Spawn explosions
        if self.explosion_frames:
            for _ in range(8):  # 8 explosion GIFs
                x = random.randint(0, 800)
                y = random.randint(0, 500)
                gif_id = self.gif_canvas.create_image(x, y, image=self.explosion_frames[0], anchor=tk.NW)
                self.gif_instances.append((gif_id, self.explosion_frames, 0))
        
        # Spawn fires
        if self.fire_frames:
            for _ in range(12):  # 12 fire GIFs
                x = random.randint(0, 800)
                y = random.randint(0, 500)
                gif_id = self.gif_canvas.create_image(x, y, image=self.fire_frames[0], anchor=tk.NW)
                self.gif_instances.append((gif_id, self.fire_frames, 0))
        
        self.animate_chaos()

    def animate_chaos(self):
        if not self.gif_active:
            return
            
        for i, (gif_id, frames, frame_idx) in enumerate(self.gif_instances):
            next_idx = (frame_idx + 1) % len(frames)
            self.gif_canvas.itemconfig(gif_id, image=frames[next_idx])
            self.gif_instances[i] = (gif_id, frames, next_idx)
            
            # Randomly move some GIFs around for extra chaos
            if random.random() < 0.1:  # 10% chance to move
                x_offset = random.randint(-20, 20)
                y_offset = random.randint(-10, 10)
                self.gif_canvas.move(gif_id, x_offset, y_offset)
        
        self.root.after(100, self.animate_chaos)

    def fade_color(self, fg, bg, opacity):
        fg_rgb = self.hex_to_rgb(fg)
        bg_rgb = self.hex_to_rgb(bg)
        mix = tuple(int(bg_c + (fg_c - bg_c) * opacity) for fg_c, bg_c in zip(fg_rgb, bg_rgb))
        return self.rgb_to_hex(mix)

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(self, rgb):
        return "#{:02x}{:02x}{:02x}".format(*rgb)

    def go_back(self):
        self.gif_active = False
        self.clear_content_frame()
        self.create_input_ui()

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        if hasattr(self, 'gif_canvas'):
            self.gif_canvas.pack_forget()
            self.gif_canvas.delete("all")


def run_app():
    root = tk.Tk()
    app = NamePredictorApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()




