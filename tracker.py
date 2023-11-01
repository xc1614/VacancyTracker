import json

# Initialize vacancies as an empty list
vacancies = []

# Load data from a file if it exists
try:
    with open('vacancies.json', 'r') as file:
        vacancies = json.load(file)
except FileNotFoundError:
    vacancies = []

# Function to add a vacancy to the tracker
def add_vacancy(agency, job_title):
    vacancies.append({'agency': agency, 'job_title': job_title, 'status': 'Open'})

# Function to list all vacancies
def list_vacancies():
    for index, vacancy in enumerate(vacancies, start=1):
        print(f"{index}. Agency: {vacancy['agency']} | Job Title: {vacancy['job_title']} | Status: {vacancy['status']}")

# Function to update the status of a vacancy with data validation
def update_status(vacancy_index, new_status):
    if 1 <= vacancy_index <= len(vacancies):
        if new_status in ['Open', 'Closed', 'In Progress']:
            vacancies[vacancy_index - 1]['status'] = new_status
        else:
            print("Invalid status. Please enter a valid status.")
    else:
        print("Invalid vacancy index.")

# Main program loop
while True:
    print("\nVacancy Tracker Menu:")
    print("1. Add a vacancy")
    print("2. List all vacancies")
    print("3. Update vacancy status")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        agency = input("Enter agency name: ")
        job_title = input("Enter job title: ")
        add_vacancy(agency, job_title)
        print("Vacancy added successfully!")

    elif choice == '2':
        list_vacancies()

    elif choice == '3':
        list_vacancies()
        vacancy_index = int(input("Enter the index of the vacancy you want to update: "))
        new_status = input("Enter the new status (e.g., Open, Closed, In Progress): ")
        update_status(vacancy_index, new_status)

    elif choice == '4':
        # Save data to a file before exiting
        with open('vacancies.json', 'w') as file:
            json.dump(vacancies, file)
        print("Exiting the Vacancy Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")