export default function updateStudentGradeByCity(students, city, newGrades) {
    return students
      .filter((student) => student.location === city)
      .map((currentStudent) => {
        const updatedRecord = { ...currentStudent };
  
        const matchedGrade = newGrades.find((grade) => grade.studentId === currentStudent.id);
        if (matchedGrade) {
          updatedRecord.grade = matchedGrade.grade;
        } else {
          updatedRecord.grade = 'N/A';
        }
  
        return updatedRecord;
      });
  }
