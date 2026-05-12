def calculate_final_grade(attendance, midterm, final):
    if attendance < 70:
        status = "Fail (Attendance)"
    else:
        # Calculate weighted average
        total_score = (midterm * 0.4) + (final * 0.6)

        # Apply a small bonus for perfect attendance
        if attendance >= 100:
            total_score = total_score + 5

        # Final grade assignment
        if total_score >= 90:
            status = "Grade: A"
            return status
        elif total_score >= 50:
            status = "Grade: Pass"
            return status
        else:
            status = "Grade: Fail (Score)"
            return status

    return status

