// Import FullCalendar and its styles
import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid'; // Import other plugins you need

// Initialize FullCalendar
document.addEventListener('DOMContentLoaded', function () {
  var calendarEl = document.getElementById('calendar'); // Replace 'calendar' with the ID of your calendar element

  var calendar = new Calendar(calendarEl, {
    plugins: [dayGridPlugin], // Add other plugins here as needed
    // Configure other options and events as per your requirements
  });

  calendar.render(); // Render the calendar
});
