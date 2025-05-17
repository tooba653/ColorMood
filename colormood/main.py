import streamlit as st
import random


class ColorMood:
    def __init__(self, color: str, quotes: list[str]):
        self.color = color.lower()
        self.quotes = quotes

    def get_random_quote(self):
        return random.choice(self.quotes)


class ColorQuoteManager:
    def __init__(self):
        self.color_moods = {}
        self._load_colors()

    def _load_colors(self):
        self.color_moods = {
            "red": ColorMood("Red", [
                "Red symbolizes passion and energy!",
                "Feeling bold? That’s the power of Red!",
                "Red sparks excitement and action."
            ]),
            "blue": ColorMood("Blue", [
                "Blue brings calm and serenity.",
                "Feeling peaceful? That’s the magic of Blue.",
                "Blue inspires trust and wisdom."
            ]),
            "green": ColorMood("Green", [
                "Green means growth and harmony.",
                "Feeling balanced? Thank Green for that!",
                "Green symbolizes renewal and nature."
            ]),
            "yellow": ColorMood("Yellow", [
                "Yellow shines with happiness and optimism.",
                "Feeling joyful? Yellow lights up your mood!",
                "Yellow sparks creativity and energy."
            ]),
            "purple": ColorMood("Purple", [
                "Purple represents luxury and wisdom.",
                "Feeling creative? Purple fuels imagination.",
                "Purple inspires mystery and magic."
            ]),
            "orange": ColorMood("Orange", [
                "Orange radiates enthusiasm and warmth.",
                "Feeling energetic? Orange boosts your spirit!",
                "Orange encourages social interaction and fun."
            ]),
            "pink": ColorMood("Pink", [
                "Pink conveys love and kindness.",
                "Feeling gentle? Pink nurtures your soul.",
                "Pink symbolizes compassion and care."
            ])
        }

    def get_quote_by_color(self, color: str):
        color = color.lower()
        if color in self.color_moods:
            return self.color_moods[color].get_random_quote()
        else:
            return None

    def available_colors(self):
        return list(self.color_moods.keys())

def main():
    st.title("🎨 ColorMood - Pick a Color, Get a Quote")
    st.write("Choose your favorite color and get a mood-boosting quote!")

    manager = ColorQuoteManager()
    colors = manager.available_colors()

    selected_color = st.selectbox("Pick a color", options=colors)

    if st.button("Get Quote"):
        quote = manager.get_quote_by_color(selected_color)
        if quote:
            st.markdown(f"### 🌟 {quote}")
        else:
            st.error("Oops! No quote found for that color.")

if __name__ == "__main__":
    main()
