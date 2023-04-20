"use strict";

const output = document.querySelector(".output");

const fakeJSONOut = {
  first_name: "Kyle",
  last_name: "Bergermeister",
  address: {
    street: "123 Sesame St",
    city: "St. Louis",
    county: "Dekalb",
    state: "MO",
    "zip code": "66207",
  },
  email: "oh@welp.org",
  phone_number: "666-420-6969",
  complaint: "This is an angry complaint",
};

const handlePython = function () {
  console.log("test");
  const fakeJSON = JSON.stringify(fakeJSONOut);
  //get JSON (we'll use a fake object for now)
  const data = JSON.parse(fakeJSON);
  console.log(data);
  //parse JSON into object

  //put object information into fields on html
  const markup = `<p>
  <strong class="field">First Name:</strong><span id="first_name" class="data">${data.first_name}</span><br />
  <strong class="field">Last Name:</strong><span id="last_name" class="data">${data.last_name}</span><br />
  <strong class="field">Address:</strong><span id="address" class="data">${data.address.street}</span><br />
  <strong class="field">City:</strong><span id="city" class="data">${data.address.city}</span><br />
  <strong class="field">State:</strong><span id="state" class="data">${data.address.state}</span><br />
  <strong class="field">Zip Code:</strong><span id="zip" class="data">${data.address["zip code"]}</span><br />
  <strong class="field">Email:</strong><span id="email" class="data">${data.email}</span><br />
  <strong class="field">Phone Number:</strong><span id="phone" class="data">${data.phone_number}</span><br />
  <strong class="field">Complaint:</strong><span id="complaint" class="data">${data.complaint}</span><br />
</p>`;
  output.innerHTML = "";
  output.insertAdjacentHTML("afterbegin", markup);
};

document.querySelector(".submission").addEventListener("click", handlePython);
