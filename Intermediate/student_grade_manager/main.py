# Student Grade Manager 

# # step 1 : get students name and score

# students_score = input('Enter student names and scores (e.g. John:85, Jane:92): ').strip()

# # step 2 : process the input to create a dictionary of student names and scores

# student_dict = {}
# for entry in students_score.split(','):
#     name, score = entry.split(':')
#     student_dict[name] = int(score)


# # step 3 : Assign grades based on scores using list comprehension

# grades = {  name:
#             'A' if score >= 90 else 
#             'B' if score >= 80 else 
#             'C' if score >= 70 else 
#             'D' if score >= 60 else 
#             'F'
#             for name, score in student_dict.items()
# }



# # step 4 : filter passing and failing students
# passing_students = {name: grade for name, grade in grades.items() if grade != 'F'}
# failing_students = {name: grade for name, grade in grades.items() if grade == 'F'}

# # step 4 : Print the results in a formatted way
# print("Student Grades:")
# for name, grade in grades.items():
#     print(f"  {name}: {grade}")

# print("\nPassing Students:")
# for name, grade in passing_students.items():
#     print(f"  {name}: {grade}")

# print("\nFailing Students:")
# for name, grade in failing_students.items():
#     print(f"  {name}: {grade}")



# ---------------------------------------------------------------------------------------------------------------------------

# updated code 

# =========================================
# Student Grade Management System (Enhanced)
# =========================================

def parse_input(user_input: str) -> dict:
    """Parse and validate student names and scores."""
    students = {}

    for entry in user_input.split(','):
        try:
            name, score = entry.split(':')
            name = name.strip()
            score = int(score.strip())

            if not name:
                raise ValueError("Empty name")

            if not 0 <= score <= 100:
                raise ValueError("Invalid score")

            students[name] = score

        except ValueError:
            print(f"⚠️ Skipping invalid entry: {entry}")

    return students


def assign_grade(score: int) -> str:
    """Assign grade based on score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def calculate_statistics(scores: dict) -> dict:
    """Calculate average, topper, and lowest scorer."""
    total_students = len(scores)
    total_score = sum(scores.values())

    average = total_score / total_students

    topper = max(scores, key=scores.get)
    lowest = min(scores, key=scores.get)

    return {
        "average": round(average, 2),
        "topper": (topper, scores[topper]),
        "lowest": (lowest, scores[lowest])
    }


def print_section(title: str, data: dict):
    """Print formatted student data."""
    print(f"\n{title}")
    if not data:
        print("  None")
        return

    for name, value in data.items():
        print(f"  {name}: {value}")


def main():
    print("\n🎓 Student Grade Management System\n")

    user_input = input(
        "Enter student names and scores (e.g. John:85, Jane:92): "
    ).strip()

    student_scores = parse_input(user_input)

    if not student_scores:
        print("\n❌ No valid student data found.")
        return

    # Assign grades
    grades = {
        name: assign_grade(score)
        for name, score in student_scores.items()
    }

    # Filter students
    passing_students = {n: g for n, g in grades.items() if g != 'F'}
    failing_students = {n: g for n, g in grades.items() if g == 'F'}

    # Calculate statistics
    stats = calculate_statistics(student_scores)

    # Display results
    print_section("📘 Student Grades:", dict(sorted(grades.items())))
    print_section("✅ Passing Students:", dict(sorted(passing_students.items())))
    print_section("❌ Failing Students:", dict(sorted(failing_students.items())))

    # Display statistics
    print("\n📊 Class Statistics:")
    print(f"  📈 Average Score : {stats['average']}")
    print(f"  🏆 Topper        : {stats['topper'][0]} ({stats['topper'][1]})")
    print(f"  🔻 Lowest Score  : {stats['lowest'][0]} ({stats['lowest'][1]})")


if __name__ == "__main__":
    main()
