import time
import webbrowser
import os

def print_slow(text, delay=0.04, color="\033[96m"):
    reset = "\033[0m"
    for char in text:
        print(f"{color}{char}{reset}", end='', flush=True)
        time.sleep(delay)
    print()

def terminal_story():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "="*50)
    print("     THE STORY OF THIRTY CROWN")
    print("="*50 + "\n")
    time.sleep(1)

    print_slow("Ek zamane me ek jadooi jungle tha...", 0.05, "\033[92m")
    time.sleep(0.8)
    print_slow("Wahan ek choti si Princess rehti thi jiska naam tha LUNA.", 0.04, "\033[93m")
    time.sleep(0.8)
    print_slow("Luna ke paas 29 crowns the, lekin 30th crown kho gaya tha.", 0.04, "\033[95m")
    time.sleep(0.8)
    print_slow("Ek din usne faisla kiya: 'Me 30th Crown dhoondh kar rahungi!'", 0.05, "\033[91m")
    time.sleep(1)
    print_slow("Raste me usko 3 dost mile - Bunny, Cat aur Star.", 0.04, "\033[94m")
    time.sleep(0.8)
    print_slow("Sab ne milkar pahad, darya paar kiye.", 0.04, "\033[96m")
    time.sleep(0.8)
    print_slow("Aakhir me unhe 30th Crown ek Rainbow ke neeche mila!", 0.05, "\033[92m")
    time.sleep(0.8)
    print_slow("Jab Luna ne 30 crowns pehne, wo Queen of Light ban gayi!", 0.05, "\033[93m")
    print_slow("Aur sab khushi khushi rehne lage. THE END.", 0.06, "\033[92m")
    print("\n" + "="*50 + "\n")
    time.sleep(2)

def chrome_story():
    html = """
<!DOCTYPE html>
<html><head><title>Thirty Crown Story</title>
<style>
body{background:#1a0033; color:white; font-family:Arial; text-align:center; padding:20px;}
h1{font-size:50px; animation:glow 2s infinite; color:gold;}
.card{background:white; color:black; border-radius:20px; padding:20px; margin:20px auto; max-width:600px; font-size:22px; animation:slide 1s;}
@keyframes glow{0%,100%{text-shadow:0 0 10px gold;} 50%{text-shadow:0 0 30px gold, 0 0 50px orange;}}
@keyframes slide{from{transform:translateY(50px); opacity:0;} to{transform:translateY(0); opacity:1;}}
.crown{font-size:60px; animation:bounce 1s infinite;}
@keyframes bounce{0%,100%{transform:translateY(0);} 50%{transform:translateY(-15px);}}
</style></head>
<body>
<h1>👑 THIRTY CROWN 👑</h1>
<div class="crown">👑✨</div>
<div class="card" style="animation-delay:0.2s">Chapter 1: Ek jadooi jungle me Princess Luna rehti thi. Uske paas 29 crowns the.</div>
<div class="card" style="animation-delay:0.6s">Chapter 2: 30th Crown kho gaya! Luna ne usko dhoondhne ka faisla kiya.</div>
<div class="card" style="animation-delay:1s">Chapter 3: Uske 3 cute dost Bunny, Cat aur Star uske saath chal pade.</div>
<div class="card" style="animation-delay:1.4s">Chapter 4: Bohat mushkilon ke baad, unhe Rainbow ke neeche 30th Crown mil gaya!</div>
<div class="card" style="background:gold; font-weight:bold; animation-delay:1.8s">Chapter 5: Luna ne 30 crowns pehne aur Queen of Light ban gayi! THE END - Happy Ending!</div>
</body></html>
"""
    with open("thirty_crown.html", "w", encoding="utf-8") as f:
        f.write(html)
    webbrowser.open(os.path.abspath("thirty_crown.html"))

terminal_story()
chrome_story()
print("Chrome me aapki story book khul gayi hai! Check karo!")