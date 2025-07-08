import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Audit Decision Tool", layout="centered")

st.title("🧪 Third-Party Audit Entscheidungshilfe")
st.markdown("Dieses Tool unterstützt GMP-konform bei der Entscheidung, ob ein **Third-Party-Audit** sinnvoll ist – aus Sicht von Auftraggeber (Auditnutzer) oder Lieferant (Auditierter).")

# Auswahl der Perspektive
rolle = st.radio("Wer nutzt das Tool?", ["Auditnutzer (Pharmaunternehmen)", "Auditierter (Lieferant)"])

st.divider()

antworten = {}
entscheidung = ""

if rolle == "Auditnutzer (Pharmaunternehmen)":
    st.subheader("🔎 Entscheidungspfad: Auditnutzer")
    antworten["a"] = st.radio("a) Genügend eigene Auditoren verfügbar?", ["Ja", "Nein"])
    if antworten["a"] == "Nein":
        entscheidung = "Third-Party-Audit empfohlen (fehlende Ressourcen)"
    else:
        antworten["b"] = st.radio("b) Genügend Erfahrung / passende Expertise vorhanden?", ["Ja", "Nein"])
        if antworten["b"] == "Nein":
            entscheidung = "Third-Party-Audit empfohlen (fehlende Expertise)"
        else:
            antworten["c"] = st.radio("c) Eigene Durchführung wirtschaftlich sinnvoll?", ["Ja", "Nein"])
            if antworten["c"] == "Nein":
                entscheidung = "Third-Party-Audit empfohlen (Kostenvorteil extern)"
            else:
                antworten["d"] = st.radio("d) Handelt es sich um ein Erstaudit?", ["Ja", "Nein"])
                if antworten["d"] == "Ja":
                    entscheidung = "Kein Third-Party-Audit empfohlen (Erstaudit)"
                else:
                    antworten["e"] = st.radio("e) Hohes Risiko beim Lieferanten?", ["Ja", "Nein"])
                    if antworten["e"] == "Ja":
                        entscheidung = "Kein Third-Party-Audit empfohlen (hohes Risiko)"
                    else:
                        antworten["f"] = st.radio("f) Vorherige Audits mit kritischen Mängeln?", ["Ja", "Nein"])
                        if antworten["f"] == "Ja":
                            entscheidung = "Kein Third-Party-Audit empfohlen (kritische Vorerfahrung)"
                        else:
                            antworten["g"] = st.radio("g) Langjähriger, GMP-konformer Lieferant?", ["Ja", "Nein"])
                            if antworten["g"] == "Ja":
                                entscheidung = "Third-Party-Audit angemessen (GMP-erprobter Lieferant)"
                            else:
                                entscheidung = "Kein Third-Party-Audit empfohlen (geringe GMP-Erfahrung)"

elif rolle == "Auditierter (Lieferant)":
    st.subheader("🔎 Entscheidungspfad: Auditierter")
    antworten["a"] = st.radio("a) Akzeptieren Kunden laut Vertrag nur persönliche Audits?", ["Ja", "Nein"])
    if antworten["a"] == "Ja":
        entscheidung = "Kein Third-Party-Audit möglich (vertraglich ausgeschlossen)"
    else:
        antworten["b"] = st.radio("b) Genug eigene Kapazitäten für individuelle Audits?", ["Ja", "Nein"])
        if antworten["b"] == "Nein":
            entscheidung = "Third-Party-Audit empfohlen (Ressourcenschonung)"
        else:
            antworten["c"] = st.radio("c) Stören viele Kundenaudits das Tagesgeschäft?", ["Ja", "Nein"])
            if antworten["c"] == "Ja":
                entscheidung = "Third-Party-Audit empfohlen (Entlastung des Betriebs)"
            else:
                antworten["d"] = st.radio("d) Ist der persönliche Kundenkontakt besonders wichtig?", ["Ja", "Nein"])
                if antworten["d"] == "Ja":
                    entscheidung = "Kein Third-Party-Audit empfohlen (Kundentransparenz gewünscht)"
                else:
                    antworten["e"] = st.radio("e) Ist Datenschutz/Vertraulichkeit oberste Priorität?", ["Ja", "Nein"])
                    if antworten["e"] == "Ja":
                        entscheidung = "Eher kein Shared Third-Party-Audit empfohlen (Datenschutz)"
                    else:
                        entscheidung = "Shared Third-Party-Audit möglich (Effizienzvorteil)"

# Ergebnisanzeige
if entscheidung:
    st.divider()
    st.subheader("📋 Ergebnis")
    st.markdown(f"**Empfehlung:** {entscheidung}")
    st.caption(f"Stand: {datetime.now().strftime('%d.%m.%Y, %H:%M Uhr')}")

    with st.expander("📄 Antworten anzeigen"):
        for key, val in antworten.items():
            st.write(f"**{key})** {val}")
