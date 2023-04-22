import React, { useState } from "react";

function Form() {
  const [height, setHeight] = useState("");
  const [age, setAge] = useState("");
  const [weight, setWeight] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("Height:", height, "Age:", age, "Weight:", weight);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Height:
        <input
          type="text"
          value={height}
          onChange={(event) => setHeight(event.target.value)}
        />
      </label>
      <br />
      <label>
        Age:
        <input
          type="text"
          value={age}
          onChange={(event) => setAge(event.target.value)}
        />
      </label>
      <br />
      <label>
        Weight:
        <input
          type="text"
          value={weight}
          onChange={(event) => setWeight(event.target.value)}
        />
      </label>
      <br />
      <button type="submit">Submit</button>
    </form>
  );
}

export default Form;
