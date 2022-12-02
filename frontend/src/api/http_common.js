import axios from 'axios';

const HTTP = axios.create({
  baseURL: process.env.NODE_ENV === 'production' ? "https://htapis-teddidodo.vercel.app" : "https://htapis-teddidodo.vercel.app",
  headers: {
    // Authorization: axios.defaults.headers.Authorization
  }
});

export default HTTP;
