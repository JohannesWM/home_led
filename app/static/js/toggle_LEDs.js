function sendData(mode_id) {

    const modes_array = ["toggleOFF", "toggleRainbow", "toggleRacer", "toggleTimer60", "toggleSpeedRacer"];

	    $.ajax({
        type: "POST",
        url: "/mode_switch",
        data: { mode: mode_id},
        success: function(response) {
        		console.log(response);
        		}
      });

      for (let i = 0; i < modes_array.length; i++) {

      var toggle_name = modes_array[i];

      if (toggle_name == mode_id) {
      var toggleIcon = document.getElementById(toggle_name);
          if (toggleIcon.classList.contains("bi-toggle-off")) {
             toggleIcon.classList.remove("bi-toggle-off");
             toggleIcon.classList.add("bi-toggle-on");
                  // Add any other desired logic when the toggle is turned on
          } else {
             toggleIcon.classList.remove("bi-toggle-on");
             toggleIcon.classList.add("bi-toggle-on");
                  // Add any other desired logic when the toggle is turned off
          }
      }

      else {

          var toggleIcon = document.getElementById(toggle_name);
              if (toggleIcon.classList.contains("bi-toggle-on")) {

                 toggleIcon.classList.remove("bi-toggle-on");
                 toggleIcon.classList.add("bi-toggle-off");
                      // Add any other desired logic when the toggle is turned on
              } else {
                 toggleIcon.classList.remove("bi-toggle-on");
                 toggleIcon.classList.add("bi-toggle-off");
                      // Add any other desired logic when the toggle is turned off
              }


      }
      }

}