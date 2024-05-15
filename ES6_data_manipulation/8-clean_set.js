
export default function cleanSet(set, startString) {
    if (
      typeof startString !== 'string'
        || typeof set !== 'object'
        || startString.length === 0
    ) {
      return '';
    }
  
    const cleanedValues = [];
    for (const value of set) {
      if (value && value.startsWith(startString)) {
        cleanedValues.push(value.slice(startString.length));
      }
    }
  
    return cleanedValues.join('-');
  }