import requests
def fetchfact(url:str):
    try:
        response=requests.get(url)
        if response.status_code==200:
            fact_data=response.json()
            print(f"Did you know?{fact_data['text']}")
        else:
            print("Failed to get fact.")
    except Exception as e:
        print(f"An error occurred:{e}")
def main():
    print("Choose a category to fetch a random fact:")
    categories={
        "1":"General Fact",
        "2":"Technology Fact",
        "3":"History Fact",
        "4":"Science Fact",
        "5":"Sports Fact",
        "6":"Music Fact",
    }
    for key,category in categories.items():
        print(f"{key}.{category}")
    while True:
        category_choice=input("\nEnter the number of the category you want a fact of (or 'q' to quit):")
        if category_choice.lower()=='q':
            print("Goodbye!")
            break
        if category_choice=="1":
            url="https://uselessfacts.jsph.pl/random.json?language=en"
        elif category_choice=="2":
            url="https://uselessfacts.jsph.pl/category/Technology.json?language=en"
        elif category_choice=="3":
            url="https://uselessfacts.jsph.pl/category/History.json?language=en"
        elif category_choice=="4":
            url="https://uselessfacts.jsph.pl/category/Science.json?language=en"
        elif category_choice=="5":
            url="https://uselessfacts.jsph.pl/category/Sports.json?language=en"
        elif category_choice=="6":
            url="https://uselessfacts.jsph.pl/category/Music.json?language=en"
        else:
            print("Invalid! Try again.")
            continue
        fetchfact(url)
        continue_choice=input("\nDo you want another fact?(yes/no):").strip().lower()
        if continue_choice!="yes":
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()