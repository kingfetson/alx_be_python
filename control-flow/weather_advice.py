# weather_advice.py
# Interactive Weather Clothing Advisor using if-elif-else and a replay option

def main():
    print("🌦️ Welcome to the Weather Clothing Advisor! 🌞☔🧥")

    while True:
        # Prompt the user for the current weather
        weather = input("\nWhat's the weather like today? (sunny/rainy/cold or 'q' to quit): ").strip().lower()

        # Allow user to exit the loop
        if weather == "q":
            print("Goodbye! Stay stylish and weather-ready! 👋")
            break

        # Provide clothing recommendations
        if weather == "sunny":
            print("😎 Wear a t-shirt and sunglasses.")
        elif weather == "rainy":
            print("☔ Don't forget your umbrella and a raincoat.")
        elif weather == "cold":
            print("🧣 Make sure to wear a warm coat and a scarf.")
        else:
            print("❌ Sorry, I don't have recommendations for this weather.")

if __name__ == "__main__":
    main()
