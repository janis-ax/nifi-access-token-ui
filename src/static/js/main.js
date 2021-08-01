function request_token() {
    let url = document.getElementById("nifi-url").value;
    url += "access";

    fetch(`${window.origin}/ping`, {
      method: "POST",
      credentials: "include",
      body: JSON.stringify({"name": "test"}),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json",
      }),
    })
      .then(function (response) {
        if (response.status !== 200) {
          console.log(
            `Looks like there was a problem. Status code: ${response.status}`
          );
          return;
        }
        response.json().then(function (data) {
          console.log(data);
        });
      })
      .catch(function (error) {
        console.log("Fetch error: " + error);
      });
  }