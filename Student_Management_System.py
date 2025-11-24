#===========================
# Student Management System
#===========================

students = []
used_ids = set()

while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. Show All Student")
    print("3. Search Student by ID")
    print("4. Delete Student by ID")
    print("5. Show Summary (count, all subject)")
    print("6. Exit")

    try:
        choice = int(input("Enter choice (1-6):"))
    except:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        # Add Student
        try:
            sid = int(input("Enter Student ID (number):"))
        except:
            print("Invalid Id. ID must be a number.")
            continue
        if sid in used_ids:
            print("This ID already exist. Try another ID.")
            continue
        name = input("Enter Student Name:").strip()
        if name == "":
            print("Name cannot be empty.")
            continue

        # Ask subjects:

        print("Enter exactly two subjects for the student.")
        sub1 = input("Subject 1:").strip()
        sub2 = input("Subject 2:").strip()
        
        if sub1 == "" or sub2 == "":
            print("Subjects cannot be empty.")
            continue
        subjects = (sub1, sub2)

        # Marks input :
        marks = {}
        valid_marks = True
        for s in subjects:
            try:
                score = int(input(f"Enter marks for {s} (0 - 100):"))
                if score < 0 or score > 100:
                    print("Marks should be between 0 and 100.")
                    valid_marks = False
                    break
                marks[s] = score
            except:
                print("Invalid marks entered.")
                valid_marks = False
                break
        if not valid_marks:
            continue

        # Create Student dictionary and save:

        student = {
            "id" : sid,
            "name" : name,
            "subject" : subjects,
            "marks" : marks
        }

        students.append(student)
        used_ids.add(sid)
        print("Student added successfully")

    elif choice == 2:
        # Show all students:
        if len(students) == 0:
            print("No students available.")
        else:
            print(f"\nTotal Students: {len(students)}")
            for s in students:
                print("\n------------------------")
                print("ID:", s["id"])
                print("Name:", s["name"])
                print("Subjects:", s["subject"])
                print("Marks:")
                for subj, m in s["marks"].items():
                    print (" ", subj, "->", m)
    
    elif choice == 3:
        # Search by ID:
        try:
            tid = int(input("Enter ID to search:"))
        except:
            print("Enter a numeric ID.")
            continue
        found = False
        for s in students:
            if s["id"] == tid:
                print("\nStudent Found:")
                print("ID:", s["id"])
                print("Name:", s["name"])
                print("Subjects:", s["subjects"])
                print("Marks:")
                for subj, m in s ["marks"].items():
                    print(" ", subj, "->", m)
                found = True
                break
        if not found:
            print("Student not found with this Id.")
    elif choice == 4:
        # Delete by ID:
        try:
            did = int(input("Enter ID to Delete: "))
        except:
            print("Enter a numeric ID.")
            continue
        deleted = False
        for s in students :
            if s["id"] == did:
                students.remove(s)
                if did in used_ids:
                    used_ids.remove(did)
                print("Student deleted.")
                deleted = True
                break
        if not deleted:
            print("No Student with that ID.")

    elif choice == 5:
        # Summary: count, all unique subjects, average per student
        total = len(students)
        print("\n-----Summary-----")
        print("Total Students:", total)
        # All subjects:
        all_subjects = set()
        for s in students:
            for sub in s["subject"]:
                all_subjects.add(sub)
        print("All Subjects in system:", all_subjects)
        # Show average marks for each student
        if total > 0:
            print("\nStudent Average:")
            for s in students:
                sm = 0 
                cnt = 0
                for val in s["marks"].values():
                    sm += val
                    cnt += 1
                avg = sm/cnt if cnt > 0 else 0

                print("ID: {} | Name: {} | Average: {:.2f}".format(s["id"], s["name"], avg) )
        else:
            print("No averages to show (no students).")
    
    elif choice == 6:
        print("Exiting program. Bye!")
        break
    else:
        print("Please choose a valid option(1-6).")
