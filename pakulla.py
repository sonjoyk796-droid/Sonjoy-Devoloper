# PAKULLA UNION - ULTIMATE APP - Sonatala, Bogura

def show_menu():
    print("\n" + "="*40)
    print(" PAKULLA UNION - ULTIMATE APP")
    print(" Sonatala, Bogura, Rajshahi")
    print("="*40)
    print("1. Union Info")
    print("2. Chairman Info")
    print("3. Pakulla Haat")
    print("4. Villages & Rivers")
    print("5. Emergency Numbers")
    print("6. Doctor List")
    print("7. Grocery Shop List")
    print("8. Mosque & Madrasa List")
    print("9. School & College List")
    print("10. Blood Donor List")
    print("11. Map & Location")
    print("12. Full Overview")
    print("0. Exit")
    print("="*40)

while True:
    show_menu()
    c = input("Enter number 0-12: ")

    if c == "1":
        print("\n--- UNION INFO ---")
        print("Name: Pakulla Union - 7 No Union")
        print("Upazila: Sonatala, District: Bogura")
        print("Division: Rajshahi Division")
        print("Area: 5953 Acre / 24.09 sq km")
        print("Villages: 16, Mouza: 12, Houses: 3908")
        print("Population: 19524, Literacy: 34.4%")
    
    elif c == "2":
        print("\n--- CHAIRMAN INFO ---")
        print("Chairman: A K M Latiful Bari Tim Sarker")
        print("Union: Pakulla, Sonatala, Bogura")
        print("Office: Pakulla Union Parishad")
    
    elif c == "3":
        print("\n--- PAKULLA HAAT ---")
        print("Pakulla Haat - Famous Traditional Haat")
        print("Location: Near Jamuna River, Sonatala")
        print("Haat Days: Weekly Big Haat")
        print("Famous for: Local products, Cattle")
    
    elif c == "4":
        print("\n--- VILLAGES & RIVERS ---")
        print("Rivers: Jamuna & Bangali River")
        print("Mouza: 12, Village: 16")
        print("Villages: Pakulla, Char Pakulla,")
        print("Hatsherpur, Pouro Pakulla etc.")
    
    elif c == "5":
        print("\n--- EMERGENCY NUMBERS ---")
        print("National Emergency: 999")
        print("Sonatala Thana: 01713-374901")
        print("Sonatala Upazila Health: 01730-324432")
        print("Union Parishad Office")
    
    elif c == "6":
        print("\n--- DOCTOR LIST - PAKULLA ---")
        print("1. Dr. Abdul Karim - MBBS - Pakulla Bazar - 017XX-XXXXXX")
        print("2. Dr. Village Doctor - Pakulla Haat - 018XX-XXXXXX")
        print("3. Sonatala Upazila Health Complex - 01730-324432")
        print("(Add real numbers with permission)")

    elif c == "7":
        print("\n--- GROCERY SHOP LIST ---")
        print("1. M/S Karim Store - Pakulla Bazar - 017XX")
        print("2. M/S Bismillah Store - Haat Area - 018XX")
        print("3. M/S Pakulla Traders - Main Road")
        print("(Add real shop name & mobile)")

    elif c == "8":
        print("\n--- MOSQUE & MADRASA LIST ---")
        print("1. Pakulla Jame Masjid - Pakulla Bazar")
        print("2. Char Pakulla Jame Masjid")
        print("3. Pakulla Hafizia Madrasa")
        print("4. Hatsherpur Jame Masjid")

    elif c == "9":
        print("\n--- SCHOOL & COLLEGE LIST ---")
        print("1. Pakulla High School - Pakulla")
        print("2. Pakulla Govt Primary School")
        print("3. Char Pakulla Primary School")
        print("4. Sonatala Degree College (Nearby)")

    elif c == "10":
        print("\n--- BLOOD DONOR LIST - PAKULLA ---")
        print("A+  : Md Rakib Hasan - Pakulla - 017XX")
        print("B+  : Md Karim - Hatsherpur - 018XX")
        print("O+  : Md Sajib - Pakulla - 019XX")
        print("AB+ : Contact Union Office")
        print("Note: Add real donors who agree")

    elif c == "11":
        print("\n--- MAP & LOCATION ---")
        print("Pakulla Union, Sonatala, Bogura")
        print("Division: Rajshahi, BD")
        print("Google Map Search: Pakulla Union Parishad")
        print("Location Link: https://maps.google.com/?q=Pakulla+Sonatala+Bogura")

    elif c == "12":
        print("\n--- FULL OVERVIEW ---")
        print("Pakulla Union - Pride of Sonatala")
        print("Area: 5953 Acre, Pop: 19524")
        print("Chairman: Latiful Bari Tim Sarker")
        print("Rivers: Jamuna & Bangali")
        print("Famous: Pakulla Haat")
        print("This App Made By Son of Pakulla - Rajshahi")

    elif c == "0":
        print("\nThank You! Pakulla Union App")
        print("Made with Love - Allah Hafez!")
        break
    
    else:
        print("\nWrong! Enter 0-12 only")
