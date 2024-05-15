export default function getStudentIdsSum(students) {
    return students.reduce((accumulator, obj) => accumulator + obj.id, 0);
  }
  