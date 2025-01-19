document.getElementById("generate").addEventListener("click", () => {
    const membersInput = document.getElementById("members");
    const groupsInput = document.getElementById("groups");
    const outputDiv = document.getElementById("output");

    const members = parseInt(membersInput.value, 10);
    const groups = parseInt(groupsInput.value, 10);

    outputDiv.innerHTML = ""; // Clear previous output

    if (isNaN(members) || isNaN(groups) || groups <= 0 || members < groups) {
        outputDiv.innerHTML = `<p class="error">Invalid input. Please ensure groups are positive and less than or equal to members.</p>`;
        return;
    }

    const membPerGroup = Math.floor(members / groups);
    let remainder = members % groups;

    const booked = new Set();
    const randomInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

    for (let i = 1; i <= groups; i++) {
        const group = [];
        for (let j = 0; j < membPerGroup; j++) {
            let member;
            do {
                member = randomInt(1, members);
            } while (booked.has(member));
            booked.add(member);
            group.push(member);
        }

        if (remainder > 0) {
            let member;
            do {
                member = randomInt(1, members);
            } while (booked.has(member));
            booked.add(member);
            group.push(member);
            remainder--;
        }

        const groupOutput = document.createElement("p");
        groupOutput.textContent = `Group ${i}: ${group.sort((a, b) => a - b).join(", ")}`;
        outputDiv.appendChild(groupOutput);
    }
});
