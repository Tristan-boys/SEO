from datetime import datetime, timedelta, timezone
import re

def generate_sitemap_xml(first_post: int, last_post: int, lastmod: datetime) -> str:
	"""
		Génère un sitemap XML pour la page d'accueil et un ensemble d'articles.
	"""

	# Format ISO 8601 avec fuseau horaire
	lastmod_iso = lastmod.isoformat()

	xml_document = \
f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset
	xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
						http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">

	<!-- Page d’accueil : priorité maximale, vérifiée à 10h00 Europe/Paris -->
	<url>
		<loc>https://i-code-nawak.fr</loc>
		<lastmod>{lastmod_iso}</lastmod>
		<changefreq>daily</changefreq>
		<priority>1.0</priority>
	</url>

	<!-- Liste des posts Nawak, tous mis à jour à la même heure -->
	<!-- priorité 0.8 pour les contenus réguliers -->
	<!-- Généré automatiquement pour plus de lisibilité -->
"""

	for i in range(first_post, last_post+1):
		xml_document += \
f"""	<url>
		<loc>https://i-code-nawak.fr/posts/nawak-{i}.html</loc>
		<lastmod>{lastmod_iso}</lastmod>
		<changefreq>daily</changefreq>
		<priority>0.8</priority>
	</url>
"""

	# Pied du sitemap
	xml_document += "</urlset>"

	# Concaténation des parties
	return xml_document


# Exemple d'utilisation : Date du 1er juillet 2025 à 10h (Europe/Paris UTC+2)
time = (2025, 7, 1, 10, 0, 0)
lastmod = datetime(*time, tzinfo=timezone(timedelta(hours=2)))

with open(f"{re.search(r".*[\\\/]", __file__)[0]}sitemap.xml", "w", encoding="UTF8") as f:
	f.write(generate_sitemap_xml(1, 30, lastmod))
