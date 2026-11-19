# Portfolio — Koffi Osias DJIBLEVO

Site statique (HTML, CSS, JavaScript), sans framework ni installation. Il s’ouvre directement dans un navigateur.

## Structure

```
index.html            page unique (toutes les sections)
css/style.css         styles : couleurs, mise en page, animations
js/main.js            textes FR/EN, compétences, projets, certifications, animations, CV
assets/images/        portrait.webp et certificats (cert-*.webp)
assets/favicon.svg    icône de l’onglet
.nojekyll             demande à GitHub Pages de servir les fichiers tels quels
```

## Voir le site en local

Ouvre `index.html` dans ton navigateur, ou lance un petit serveur :

```
python -m http.server 8000
```

puis va sur http://localhost:8000.

## Modifier le contenu

Tout se passe dans `js/main.js` :

| Quoi | Où |
|---|---|
| Textes du site (français et anglais) | objet `D` (`fr` et `en`) |
| Compétences | tableau `SK` |
| Projets (statut, description, tags, lien) | tableau `PJ` : `s` = `done`, `progress` ou `planned` ; `l` = lien GitHub |
| Certifications | tableau `CR` ; ajoute l’image dans `assets/images/` et dans l’objet `IMG` |
| Contenu du lab | tableau `LAB` |
| CV téléchargeable | fonction `buildCV` |

Autres réglages :

- **Couleurs** : variables au début de `css/style.css` (`--ac` est la couleur d’accent, bloc `:root[data-theme="light"]` pour le thème clair).
- **Photo** : remplace `assets/images/portrait.webp` (de préférence détourée, fond transparent, visage dans la moitié haute).
- **Email, GitHub, LinkedIn** : section `#contact` de `index.html`.
- **Captures de projets** : ajoute-les dans `assets/images/` puis affiche-les dans les cartes de `PJ`.

## Publier gratuitement sur GitHub Pages

1. Sur GitHub, crée un dépôt public. Nom `Osias-DJIBLEVO.github.io` pour obtenir l’adresse `https://osias-djiblevo.github.io`, ou n’importe quel autre nom (l’adresse sera alors `https://osias-djiblevo.github.io/nom-du-depot/`).
2. Envoie tous les fichiers de ce dossier à la racine du dépôt :
   ```
   git init
   git add .
   git commit -m "Portfolio"
   git branch -M main
   git remote add origin https://github.com/Osias-DJIBLEVO/NOM-DU-DEPOT.git
   git push -u origin main
   ```
3. Dans le dépôt : **Settings → Pages → Build and deployment**, choisis **Deploy from a branch**, branche `main`, dossier `/ (root)`, puis **Save**.
4. Attends une à deux minutes : l’adresse du site s’affiche en haut de la page Pages.

Chaque `git push` met le site à jour.

## À savoir

- Les polices viennent de Google Fonts : sans connexion, le site utilise des polices système.
- Le bouton « Télécharger le CV » produit un fichier HTML ; ouvre-le puis imprime-le en PDF.
- Les certificats affichent leurs identifiants : retire-les des images si tu préfères ne pas les publier.
