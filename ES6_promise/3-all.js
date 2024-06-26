import { createUser, uploadPhoto } from './utils';

export default async function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      console.log(results[0].body, results[1].firstName, results[1].lastName);
    })

    .catch(() => console.log('Signup system offline'));
}
