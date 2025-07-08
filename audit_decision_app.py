import streamlit as st

st.set_page_config(page_title="Audit Decision Tool", layout="centered")

st.title("🧪 Audit-Entscheidungshilfe")
st.write("Beantworten Sie die folgenden Fragen, um zu entscheiden, ob ein **Third-Party-Audit** erforderlich ist.")

# Frage a
ressourcen = st.radio("a) Hat das eigene Unternehmen genügend personelle Ressourcen (qualifizierte Auditoren)?", ["Ja", "Nein"])
if ressourcen == "Nein":
    st.success("✅ Empfehlung: Third-Party-Audit")
    st.stop()

# Frage b
auditoren = st.radio("b) Sind die Auditoren für das vorgesehene Audit geeignet (Erfahrung, Expertise)?", ["Ja", "Nein"])
if auditoren == "Nein":
    st.success("✅ Empfehlung: Third-Party-Audit")
    st.stop()

# Frage c
kosten = st.radio("c) Sind die Kosten bei eigener Durchführung vertretbar?", ["Ja", "Nein"])
if kosten == "Nein":
    st.success("✅ Empfehlung: Third-Party-Audit")
    st.stop()

# Frage d
erstaudit = st.radio("d) Handelt es sich um ein Erstaudit bei einem neuen Lieferanten?", ["Ja", "Nein"])
if erstaudit == "Ja":
    st.success("✅ Empfehlung: Third-Party-Audit")
    st.stop()

# Frage e
risiko = st.radio("e) Welches Risiko ist mit dem Lieferanten verbunden?", ["Hohes Risiko", "Niedriges Risiko"])
if risiko == "Hohes Risiko":
    st.success("✅ Empfehlung: Third-Party-Audit")
    st.stop()

# Frage f
kritische_maengel = st.radio("f) Wie ist das letzte Audit verlaufen (kritische Mängel)?", ["Ja, kritische Mängel", "Nein"])
if kritische_maengel == "Ja, kritische Mängel":
    st.success("✅ Empfehlung: Third-Party-Audit")
    st.stop()

# Frage g
bekannter_lieferant = st.radio("g) Gut bekannter Lieferant mit hoher GMP-Compliance?", ["Ja", "Nein"])
if bekannter_lieferant == "Ja":
    st.info("ℹ️ Empfehlung: Kein Third-Party-Audit erforderlich")
else:
    st.success("✅ Empfehlung: Third-Party-Audit")
