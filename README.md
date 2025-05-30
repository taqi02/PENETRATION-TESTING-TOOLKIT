# PENETRATION-TESTING-TOOLKIT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: ANSARI MOHD TAKI 

*INTERN ID*: CT04DL765

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DISCRIPTION*:  

1. Brute‑Forcer and Login Server

For the first half of my Pen Testing Toolkit I built a tiny Flask web server that pretends to be a real‑world sign‑in page. The server listens on 127.0.0.1, port 5000, and exposes a single endpoint at /login. Instead of talking to a database, the code simply compares whatever a client submits to one hard‑coded pair of credentials: user “taqi” with password “taqi0902”. When both strings line up, the server sends back the text Login successful, any mismatch triggers a Login failed reply plus an HTTP 401 status. Building it this way let me experiment freely without risking anybody’s real data.

To attack my own server I wrote a Python brute‑forcer. The script reads a word‑list file, loops through each candidate password, and fires a POST request at /login alongside the fixed username “taqi”. The moment the response includes the success message the loop stops and prints the winning password. Running that script showed in practice why production sites need rate limits, account‑lock timers, or CAPTCHA.

I tested everything in VS Code and IDLE. VS Code’s integrated terminal made it easy to keep the Flask server in one tab while the brute‑forcer ran in another, and its debugger was a lifesaver when I accidentally pointed to the wrong host or mixed up request payloads. IDLE was handy for quick, isolated tests whenever I wanted to inspect a single function call or verify return values.

Along the way I hit the usual bump forgotten POST vs GET, typos in URLs, and the classic “connection refused” when another process already owned port 5000. Each hiccup nudged me to dig deeper into how Flask binds to the loopback address, how browsers treat POST endpoints, and how HTTP status codes guide error handling. Whenever I got stuck I leaned on resources like TutorialsPoint, DigitalOcean’s community docs, Python .org, and a handful of GitHub Gists shared by other developers, these sites filled in gaps more quickly than searching blindly.

2. Port Scanner

The toolkit’s second module is a lightweight Port Scanner built with Python’s socket library. I wanted a utility that could sweep a host again using IP 198.162.1.1 and flag whichever ports respond. The script cycles through a user‑defined range, tries to open a TCP connection on each port, and adds any successful handshakes to a list of “open” ports.

Putting the pieces together, the scanner acts as the reconnaissance stage find the door while the brute‑forcer represents the attack phase try to unlock that door. Writing both tools myself, watching packets succeed or fail, and fixing each snag taught me more than any tutorial alone could. The project sharpened my understanding of sockets, HTTP mechanics, and defensive measures that real applications should adopt to stay safe.

*OUTPUT*

![Image](https://github.com/user-attachments/assets/25ee9356-df59-4f1b-b844-1c66d9cd34c9)

![Image](https://github.com/user-attachments/assets/b865f5f0-d59f-4ab4-b95e-a0bbb854d368)

![Image](https://github.com/user-attachments/assets/34ba26c2-f8cd-4112-87b7-7425785730d0)

![Image](https://github.com/user-attachments/assets/9b69ea56-00a5-4de8-a541-d733d7e28556)

![Image](https://github.com/user-attachments/assets/fa5186df-34fb-4be6-9cd7-e20d16b7c7ab)

![Image](https://github.com/user-attachments/assets/b2956305-eb94-4ad7-b8e5-a0a5a34825cc)

![Image](https://github.com/user-attachments/assets/ed6b7776-25c3-48dd-9490-f87fd4549ec7)
