document.addEventListener("DOMContentLoaded", () => {
  const leadSelect = document.getElementById("lead_select");
  const agedInput = document.getElementById("student_aged");
  const schoolInput = document.getElementById("school");
  const channelInput = document.getElementById("detail_channel");

  async function loadLead(leadId) {
    if (!leadId) {
      agedInput.value = "";
      schoolInput.value = "";
      channelInput.value = "";
      return;
    }

    const res = await fetch(`/api/leads/${leadId}/`);
    if (!res.ok) {
      console.error("API error:", res.status);
      return;
    }

    const data = await res.json();
    agedInput.value = data.student_aged ?? "";
    schoolInput.value = data.school ?? "";
    channelInput.value = data.detail_channel ?? "";
  }

  leadSelect.addEventListener("change", (e) => loadLead(e.target.value));
});
