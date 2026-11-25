# Génère le CV d'une page (A4) : python build_cv.py  (nécessite reportlab : pip install reportlab)
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.pdfmetrics import stringWidth as sw_

OUT = "CV-Osias-DJIBLEVO.pdf"   # fichier produit à côté du script
PHONE = "+229 01 49 88 09 05"   # s'affiche dans le pied de page
NAME, TITLE = "Koffi Osias DJIBLEVO", "Étudiant en Réseaux et Cybersécurité"
EMAIL, GH, LI = "osiasdjiblevo49@gmail.com", "Osias-DJIBLEVO", "osias-djiblevo-473601328"
W, H = A4
DARK, SLATE, SIDE = HexColor("#12162A"), HexColor("#3A4660"), HexColor("#F2F3F7")
INK, MUT, ACC, LINE = HexColor("#1A1D29"), HexColor("#5A6070"), HexColor("#5B3FE0"), HexColor("#C9CDD8")

SIDEBAR = [
 ("COMPÉTENCES TECHNIQUES", [
  ("Réseaux & Protocoles", ["Cisco : VLAN, trunk DTP", "Packet Tracer", "Analyse de paquets (Wireshark)", "HTTP/HTTPS, FTP, SSH, DNS"]),
  ("Systèmes", ["Windows Server, Active Directory", "Virtualisation (Hyper-V)", "IIS, certificats, DNSSEC", "Linux (bases)"]),
  ("Bases de données", ["MySQL", "MariaDB : installation, sécurisation"]),
  ("Programmation", ["C", "Python", "Modélisation UML, Merise"]),
  ("Sécurité", ["Sécurité offensive (en apprentissage)", "Durcissement d’un serveur MariaDB", "Scanner de ports en Python", "Fortinet NSE 1, 2 et 3 (certifié)"]),
  ("Outils", ["Wireshark, Packet Tracer", "Hyper-V, VirtualBox, VMware", "Git, GitHub", "Docker (bases)"]),
 ]),
 ("QUALITÉS PERSONNELLES", [(None, ["Curiosité technique", "Apprentissage en autonomie", "Rigueur, esprit de documentation"])]),
 ("LANGUES", [(None, ["Français : courant", "Anglais : débutant"])]),
 ("CENTRES D’INTÉRÊT", [(None, ["Football", "Musique", "Cuisine"])]),
]
PROFIL = ("Étudiant en Licence 3 Informatique et Réseaux de Télécommunications à l’ESGIS Cotonou, je me forme à la sécurité "
 "offensive et au test d’intrusion. Je pratique en laboratoire (Windows Server, Hyper-V, Wireshark, Python) et je prépare mes "
 "premières certifications. Je recherche un stage en sécurité informatique afin de mettre mes compétences au service d’une "
 "équipe spécialisée en sécurité des systèmes et réseaux.")
PROJETS = [
 ("2026", "Scanner de ports TCP en Python", "Personnel", "Projet personnel · Python, sockets, multithreading",
  ["Analyse multithread des ports et récupération des bannières de services", "Export des résultats au format JSON, quatre versions successives"],
  ("Code source : ", "github.com/%s/port-scanner" % GH, "https://github.com/%s/port-scanner" % GH)),
 ("2026", "Installation et sécurisation d’un serveur MariaDB", "ESGIS", "Travaux pratiques · MariaDB, sécurisation (TP de groupe)",
  ["Installation du serveur de bases de données et mesures de sécurisation", "Compte rendu documenté et publié en ligne"],
  ("Compte rendu : ", "github.com/%s/TP_MariaDB" % GH, "https://github.com/%s/TP_MariaDB" % GH)),
 ("2026", "Laboratoire Windows Server sous Hyper-V", "Personnel", "Projet personnel · Windows Server, Hyper-V, Active Directory",
  ["Domaine Active Directory, serveur web IIS, certificats et DNSSEC", "Réseau virtuel pour s’exercer à l’administration et à la sécurité"], None),
 ("2026", "Analyse de paquets avec Wireshark", "ESGIS", "Travaux pratiques · Wireshark, TCP/IP",
  ["Capture et analyse d’une connexion web de bout en bout", "Utilisation des filtres de capture et d’affichage"], None),
]
FORMATION = [
 ("2026 – 2027 (en cours)", "Licence 3 – Informatique et Réseaux de Télécommunications", "ESGIS Cotonou · Bénin",
  ["Réseaux, systèmes, bases de données, virtualisation et cybersécurité"]),
 ("2025 – 2026", "Licence 2 – Informatique et Réseaux de Télécommunications", "ESGIS Cotonou · Bénin",
  ["Réseaux, programmation, bases de données et systèmes"]),
]
CERTS = [
 ("Nov. 2026", "Fortinet NSE 1, NSE 2 et NSE 3 Certified in Cybersecurity", "Fortinet Training Institute", ["Fondamentaux de la cybersécurité et de la sécurité réseau", "Validité jusqu’en novembre 2028"]),
 ("Nov. 2026", "COFPS – Spécialiste en Prévention de la Fraude en Ligne", "Hack & Fix Academy", ["Détection et prévention de la fraude en ligne"]),
 ("Oct. 2026", "Introduction à la cybersécurité", "Cisco Networking Academy", ["Fondamentaux de la cybersécurité : menaces, défense, bonnes pratiques"]),
 ("Févr. 2026", "Base de données MySQL · Linux pour débutant", "Cursa · Grafikart.fr, Bertrand Tech", ["Cours suivis : 1 h 07 (MySQL) et 17 min (Linux)"]),
 ("En cours", "Python – certification freeCodeCamp", "freeCodeCamp", ["Exercices de la certification Python en cours"]),
 ("Objectifs", "CEH puis OSCP", "EC-Council · OffSec", ["Préparation à la sécurité offensive et au test d’intrusion"]),
]

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("CV – " + NAME); c.setAuthor(NAME); c.setSubject("Curriculum vitae")
HB, HR, HI = "Helvetica-Bold", "Helvetica", "Helvetica-Oblique"
HEAD, FOOT = 108, 30
# bandeaux
c.setFillColor(DARK); c.rect(0, H - HEAD, W, HEAD, fill=1, stroke=0)
c.setFillColor(SIDE); c.rect(0, FOOT, 190, H - HEAD - FOOT, fill=1, stroke=0)
c.setFillColor(SLATE); c.rect(0, 0, W, FOOT, fill=1, stroke=0)
c.setFillColor(white); c.setFont(HB, 25); c.drawCentredString(W / 2, H - 52, NAME)
c.setFont(HB, 12.5); c.setFillColor(HexColor("#E3E6F0")); c.drawCentredString(W / 2, H - 76, TITLE)
c.setFillColor(ACC); c.rect(W / 2 - 24, H - 90, 48, 2.2, fill=1, stroke=0)

# colonne gauche
x0, sw = 22, 146; y = H - HEAD - 24
def item(txt, x, y, width, size=7.6, lead=10):
    lines = simpleSplit(txt, HR, size, width - 10)
    c.setFillColor(MUT); c.setFont(HR, size)
    for i, ln in enumerate(lines):
        if i == 0: c.drawString(x + 1, y, "•")
        c.drawString(x + 10, y, ln); y -= lead
    return y
for title, groups in SIDEBAR:
    c.setFillColor(DARK); c.setFont(HB, 8); c.drawString(x0, y, title)
    c.setStrokeColor(ACC); c.setLineWidth(1); c.line(x0, y - 4, x0 + sw, y - 4); y -= 17
    for g, its in groups:
        if g: c.setFillColor(INK); c.setFont(HB, 8.4); c.drawString(x0, y, g); y -= 11.5
        for t in its: y = item(t, x0, y, sw)
        y -= 6
    y -= 4

# colonne droite
x1, mw = 208, 368; y = H - HEAD - 24
def heading(t):
    global y
    y -= 5
    c.setFillColor(ACC); c.rect(x1, y - 3, 2.6, 13, fill=1, stroke=0)
    c.setFillColor(DARK); c.setFont(HB, 11); c.drawString(x1 + 8, y, t)
    c.setStrokeColor(LINE); c.setLineWidth(.6); c.line(x1, y - 6, x1 + mw, y - 6); y -= 20
def entry(date, title, tag, sub, bullets, link=None):
    global y
    c.setFillColor(INK); c.setFont(HB, 9); c.drawString(x1, y, title)
    if tag:
        tw = sw_(title, HB, 9) + 7; w = sw_(tag, HB, 6.3) + 9
        c.setFillColor(SLATE); c.roundRect(x1 + tw, y - 2, w, 9.5, 4.2, fill=1, stroke=0)
        c.setFillColor(white); c.setFont(HB, 6.3); c.drawString(x1 + tw + 4.5, y + 0.6, tag)
    if date:
        c.setFillColor(MUT); c.setFont(HI, 7); c.drawRightString(x1 + mw, y, date)
    y -= 10.2
    c.setFillColor(MUT); c.setFont(HI, 7.6); c.drawString(x1, y, sub); y -= 10
    c.setFont(HR, 7.8)
    for b in bullets:
        for i, ln in enumerate(simpleSplit(b, HR, 7.8, mw - 10)):
            c.setFillColor(INK); c.setFont(HR, 7.8)
            if i == 0: c.drawString(x1, y, "–")
            c.drawString(x1 + 8, y, ln); y -= 9.8
    if link:
        pre, shown, url = link
        c.setFillColor(INK); c.setFont(HR, 7.8); c.drawString(x1, y, "–"); c.drawString(x1 + 8, y, pre)
        px = x1 + 8 + sw_(pre, HR, 7.8); c.setFillColor(ACC); c.setFont(HB, 7.8); c.drawString(px, y, shown)
        c.linkURL(url, (px, y - 2, px + sw_(shown, HB, 7.8), y + 8), relative=0); y -= 9.8
    y -= 6
heading("Profil")
c.setFillColor(INK); c.setFont(HR, 7.9)
for ln in simpleSplit(PROFIL, HR, 7.9, mw): c.drawString(x1, y, ln); y -= 10
y -= 6
heading("Projets Académiques & Pratiques")
for p in PROJETS: entry(*p)
heading("Formation")
for f in FORMATION: entry(f[0], f[1], None, f[2], f[3])
heading("Certifications")
for k in CERTS: entry(k[0], k[1], None, k[2], k[3])
print("fin du contenu à y =", round(y), "(limite", FOOT + 8, ")")

# pied de page : contacts cliquables
parts = [(EMAIL, "mailto:" + EMAIL), ("github.com/" + GH, "https://github.com/" + GH),
         ("linkedin.com/in/" + LI, "https://www.linkedin.com/in/%s/" % LI), ("Cotonou, Bénin", None)]
if PHONE: parts.insert(1, (PHONE, None))
sep = "   ·   "; size = 7.2
total = sum(sw_(t, HR, size) for t, _ in parts) + sw_(sep, HR, size) * (len(parts) - 1)
x = (W - total) / 2; c.setFillColor(white); c.setFont(HR, size)
for i, (t, u) in enumerate(parts):
    c.drawString(x, 11, t)
    if u: c.linkURL(u, (x, 8, x + sw_(t, HR, size), 19), relative=0)
    x += sw_(t, HR, size)
    if i < len(parts) - 1: c.drawString(x, 11, sep); x += sw_(sep, HR, size)
c.showPage(); c.save(); print("OK", OUT)
