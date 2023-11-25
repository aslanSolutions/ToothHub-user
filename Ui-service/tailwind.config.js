  // tailwind.config.js
  module.exports = {
    purge: [],
    purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
     darkMode: false, // or 'media' or 'class'
     theme: {
       extend: {
        fontFamily: {
          inter: ['Inter', 'sans-serif'],
        },
       },
     },
     variants: {
       extend: {
        fontFamily: {
          inter: ['Inter', 'sans-serif'],
       },
     },
     plugins: [],
   }
   };