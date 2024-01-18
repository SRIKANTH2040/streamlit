import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def get_images(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Replace this with the specific scraping logic for image URLs on the webpage
            # Here, we are just fetching all image tags and extracting their source URLs
            img_tags = soup.find_all('img')
            img_urls = [img['src'] for img in img_tags]
            return img_urls
        else:
            return []
    except Exception as e:
        return []

# Streamlit UI
st.title("Web Scraper Image Viewer")
url_input = st.text_input("Enter URL:")
if st.button("Scrape Images"):
    if url_input:
        image_urls = get_images(url_input)
        if image_urls:
            st.write(f"Found {len(image_urls)} images:")
            for img_url in image_urls:
                try:
                    response = requests.get(img_url)
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption=f"Image from {img_url}", use_column_width=True)
                except Exception as e:
                    st.warning(f"Error displaying image from {img_url}: {str(e)}")
        else:
            st.warning("No images found on the webpage.")
    else:
        st.warning("Please enter a valid URL.")
