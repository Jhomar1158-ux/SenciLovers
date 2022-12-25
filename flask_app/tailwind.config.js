/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        'ubuntu-light': ['ubuntu-light', ...defaultTheme.fontFamily.sans],
        'ubuntu-regular': ['ubuntu-regular', ...defaultTheme.fontFamily.sans],
        'ubuntu-medium': ['ubuntu-medium', ...defaultTheme.fontFamily.sans],
        'ubuntu-bold': ['ubuntu-bold', ...defaultTheme.fontFamily.sans]
      },
      width: {
        'pantallaRaspX': '480px',
      },
      height: {
        'pantallaRaspY': '320px',
      },
      colors:{
        'senciBlue':"#0B0743",
        'senciGreen':"#89C400",
        'senciOrange':"#E8684B"
      }
    },
  },
  plugins: [],
}