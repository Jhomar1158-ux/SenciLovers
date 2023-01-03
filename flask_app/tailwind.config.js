/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      width: {
        'pantallaRaspX': '480px',
      },
      height: {
        'pantallaRaspY': '320px',
      },
      colors:{
        'senciBlue':"#0B0743",
        'senciGreen':"#89C400",
        'senciOrange':"#E8684B",
        'senciGrey': "#2E313C"
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}