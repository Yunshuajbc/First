import tkinter as tk
import random

messages = [
    "我想你了！❤️❤️", "我好想你~❤️❤️", "也有好好吃饭❤️❤️", "照顾好自己❤️❤️",
    "记得多吃水果，补充维生素哦。❤️❤️", "每天都要开开心心的哦❤️❤️", "期待下次的见面❤️❤️",
    "生日快乐！！！！❤️❤️", "顺顺利利， 万事如意❤️❤️", "乖乖等我，马上就到。❤️❤️",
    "生日快乐，宝贝❤️❤️", "我们少熬夜好不好❤️❤️", "要多喝水哦~❤️❤️", "不要不开心嘛❤️❤️",
    "保持好心情，一切都会越来越好。❤️❤️", "保持好心情哦。我来找你玩了哦❤️❤️",
    "今天有没有想我呀？我很想你。❤️❤️", "我在想你。快来找我玩❤️❤️", "保持微笑呀❤️❤️",
    "好好穿衣服哦❤️❤️", "今天有没有开心嘛❤️❤️", "今晚的星星，像你眼睛一样明亮❤️❤️",
    "不开心要和我讲呀❤️❤️", "看到什么都想分享给你❤️❤️", "一起长命百岁呀❤️❤️",
    "我不管，你要记得想我❤️❤️", "是谁这么可爱！！！是你呀！❤️❤️",
    "最最最最最最最最最最最喜欢你了！！！❤️❤️", "现在超级想你怎么办？❤️❤️",
    "有没有想我，你要想我知道吗？❤️❤️", "哈哈哈哈哈，开心！❤️❤️", "明天就要见面了！！！❤️❤️"
]
colors = ["lightpink", "lightblue", "lightyellow", "lightgreen", "lavender", "peachpuff", "mistyrose", "lightcyan"]

def show_warn_tip(root):
    window = tk.Toplevel(root)
    window.title("提示")
    message = random.choice(messages)
    color = random.choice(colors)
    width = random.randint(250, 400)
    height = random.randint(90, 140)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = random.randint(0, max(100, screen_width - width))
    y = random.randint(0, max(100, screen_height - height))
    window.geometry(f"{width}x{height}+{x}+{y}")
    label = tk.Label(window, text=message, bg=color, fg="black", 
                     font=("Microsoft YaHei", 12, "bold"), wraplength=350, justify="center")
    label.pack(expand=True, fill="both")
    window.after(5000, window.destroy)

def create_popups(root, count):
    if count > 0:
        show_warn_tip(root)
        root.after(100, lambda r=root, c=count-1: create_popups(r, c))

def main():
    root = tk.Tk()
    root.withdraw()
    create_popups(root, 50)
    root.mainloop()

if __name__ == "__main__":
    main()

