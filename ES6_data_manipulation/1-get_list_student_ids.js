export default function getListStudentIds(Objects) {
    if (!Array.isArray(Objects)) {
      return [];
    }
  
    return Objects.map((Obj) => Obj.id);
  }