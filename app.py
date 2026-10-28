import os
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "perovskite-energy-secret-2026")

# Profile Information for Dr. Laxman Gouda
PROFILE = {
    "name": "Dr. Laxman Gouda",
    "honorific": "Dr.",
    "pronouns": "He / Him",
    "title": "Co-Founder & CEO, ABX3PV | Ramanujan Fellow at IISc Bangalore",
    "headline": "Industrial-Scale Next-Generation Hybrid Perovskite Solar Cell Modules & Clean Fuels",
    "bio": "Scientist, entrepreneur, and Ramanujan Fellow at the Indian Institute of Science (IISc). Leading ABX3PV to commercialize indigenous perovskite solar cell modules on flexible and sheet substrates, silicon/perovskite tandems, and clean solar fuels.",
    "location": "Indian Institute of Science (IISc), Bangalore, India",
    "email": "laxmangouda@iisc.ac.in",
    "linkedin": "https://www.linkedin.com/in/dr-laxman-gouda-49878337/",
    "fellowship": "Marie Curie ITN Fellow & Ramanujan Fellow",
    "startup": "ABX3PV Private Limited",
    "avatar": "images/photo.jpg",
}

STATS = [
    {"number": "BRICS 2026", "label": "Bharat Innovate Finalist"},
    {"number": "Global JV", "label": "France | India | Switzerland"},
    {"number": "VivaTech", "label": "Global India Pavilion Showcase"},
    {"number": "Winner", "label": "Avaana Capital Grand Challenge"},
]

# Image Slider Data for Events, Lab Prototyping & Strategic Partnerships
SLIDES = [
    {
        "id": 1,
        "image": "images/slider-jv-mou-signing.jpg",
        "title": "Tri-National Joint Venture MoU Signing",
        "badge": "Strategic International JV",
        "caption": "Historic MoU signing to establish a trilateral Joint Venture between GenesInk (France), ABX3 PV (India), and Perovskia (Switzerland) at Bharat Innovates 2026 to scale advanced perovskite photovoltaic technologies globally.",
    },
    {
        "id": 2,
        "image": "images/slider-lab-prototype.jpg",
        "title": "Dr. Laxman Gouda with Indigenous Perovskite Solar Module",
        "badge": "Lab-to-Scale Fabrication",
        "caption": "Dr. Laxman Gouda in the laboratory showcasing an indigenously engineered, large-area multi-cell hybrid perovskite solar module with integrated interconnects and electrical output leads.",
    },
    {
        "id": 3,
        "image": "images/slider-booth-showcase.jpg",
        "title": "ABX3PV Pavilion at Bharat Innovates 2026 (Booth 102)",
        "badge": "Energy, Climate & Sustainability",
        "caption": "Exhibiting flexible continuous roll solar cells, glass-based modules, and silicon/perovskite tandem architectures to international delegates and industry leaders at Bharat Mandapam.",
    },
    {
        "id": 4,
        "image": "images/slider-prototypes-showcase.jpg",
        "title": "ABX3PV Industrial & Flexible Solar Prototypes",
        "badge": "Live Working Prototypes",
        "caption": "Live working demonstrations of sheet-to-sheet perovskite modules, continuous roll-to-roll flexible substrates, tandem cells, and solar-driven systems at the BRICS Summit.",
    },
    {
        "id": 5,
        "image": "images/slider-perovskite-space.jpg",
        "title": "Perovskite Photovoltaics for Space Applications",
        "badge": "Frontier Innovation",
        "caption": "Working satellite prototype equipped with radiation-tolerant, high-power-to-weight ratio perovskite solar cells engineered for extreme orbital and space environments.",
    },
    {
        "id": 6,
        "image": "images/slider-brics-team.jpg",
        "title": "Bharat Innovate 2026 at Bharat Mandapam",
        "badge": "BRICS Summit 2026",
        "caption": "Selected among the 39 deep-tech innovators nationwide presenting India's frontier clean-energy technology to global leaders and business delegations.",
    },
    {
        "id": 7,
        "image": "images/slider-brics-banner.jpg",
        "title": "BRICS India 2026 | Bharat Innovates",
        "badge": "National Platform",
        "caption": "Official platform honoring academia-led deep-tech startups advancing indigenous high-efficiency energy and manufacturing capabilities.",
    },
]

# Recent Milestones & Recognitions - Exactly 6 items (Equal 2x3 balanced grid)
RECENT_HIGHLIGHTS = [
    {
        "id": "tri-national-jv",
        "title": "Trilateral Joint Venture: GenesInk (France) – ABX3 PV (India) – Perovskia (Switzerland)",
        "venue": "Bharat Innovates 2026, New Delhi",
        "badge": "International JV MoU",
        "date": "Strategic Partnership",
        "summary": "Historic trilateral Joint Venture established between leading French, Indian, and Swiss clean-tech pioneers.",
        "details": "Signed an international MoU to combine specialized nanomaterial inks, scalable perovskite manufacturing, and precision device integration, establishing a global pathway for next-generation solar cells."
    },
    {
        "id": "brics-2026",
        "title": "Selected for Bharat Innovate 2026 at BRICS Summit",
        "venue": "Bharat Mandapam, New Delhi",
        "badge": "Global Summit Showcase",
        "date": "2026",
        "summary": "Selected as one of only 39 teams nationwide representing India’s frontier deep-tech innovation at the BRICS Summit Business Forum.",
        "details": "Demonstrated indigenously engineered working prototypes across four frontier domains: Perovskite solar cell modules & panels, flexible perovskite solar cells, large-area high-efficiency silicon/perovskite tandem solar cells, and specialized perovskite modules for space applications. Recognized by the Ministry of Education, BRICS Summit, and ITPO for converting frontier lab research into commercial reality."
    },
    {
        "id": "vivatech-paris",
        "title": "Representing Indian Deep-Tech at VivaTech Paris",
        "venue": "Paris, France — India Pavilion",
        "badge": "Historic First for India",
        "date": "Global CleanTech",
        "summary": "Selected as one of just 30 deep-tech startups to represent India's innovation ecosystem at the world's premier tech event.",
        "details": "Marked a historic first for India — the first time a homegrown Indian perovskite solar-cell product was showcased on a global platform of this scale. Established strategic international dialogues with global partners and clean-tech investors to accelerate the Make in India solar vision."
    },
    {
        "id": "avaana-capital",
        "title": "Winner — Avaana Capital Grand Challenge",
        "venue": "National Climate & DeepTech Innovation",
        "badge": "Grand Challenge Winner",
        "date": "Award & Grant",
        "summary": "Recognized as a Winner among the Top 12 finalists for visionary innovation in scalable clean energy.",
        "details": "Selected by an esteemed jury of climate-tech leaders and venture investors for ABX3PV's impactful, scalable approach to continuous perovskite solar manufacturing and decarbonization solutions."
    },
    {
        "id": "nanotech-award",
        "title": "Pioneering Concept Award in Nanoscience & Nanotechnology",
        "venue": "Nanoscience & Nanotechnology Forum",
        "badge": "Distinguished Recognition",
        "date": "Honor & Award",
        "summary": "Honored for pioneering concepts in nanoscale materials and advanced photovoltaic interfaces.",
        "details": "Awarded by a distinguished panel of industry leaders, research experts, and venture capitalists for demonstrating the transformative commercial potential of nanotechnology in clean energy."
    },
    {
        "id": "ramanujan-fellowship",
        "title": "Ramanujan Fellowship & Green Energy Leadership",
        "venue": "Indian Institute of Science (IISc), Bangalore",
        "badge": "National Fellowship",
        "date": "Fellowship Program",
        "summary": "Awarded national prestigious fellowship advancing next-generation solar energy and hydrogen synthesis.",
        "details": "Leading cutting-edge research at IISc Bangalore on scalable manufacturing protocols for perovskite solar modules, photo-electrosynthesis of green hydrogen, and direct catalytic capture of CO2 converted into high-density fuels."
    }
]

# Core Ventures & Flagship Research - Exactly 4 items (Equal 2x2 balanced grid)
PROJECTS = [
    {
        "id": 1,
        "title": "ABX3PV Private Limited — Scaled Solar Modules",
        "subtitle": "Co-Founder & CEO | IISc Deep-Tech Startup",
        "description": "Developing industrial-scale manufacturing of Next-generation Hybrid Perovskite solar cell modules on both Sheet-to-Sheet and continuous Roll-to-Roll flexible substrates.",
        "tags": ["Perovskite PV", "Roll-to-Roll", "CleanTech", "Industrial Scale", "DeepTech"],
        "link": "https://www.linkedin.com/in/dr-laxman-gouda-49878337/",
        "badge": "Active Startup"
    },
    {
        "id": 2,
        "title": "Green Hydrogen & CO2-to-Chemicals Synthesis",
        "subtitle": "Ramanujan Fellowship Research | IISc Bangalore",
        "description": "Pioneering the photo-electrosynthesis of green hydrogen and direct chemical capture of carbon dioxide stored into high-density chemical bonds for next-generation sustainable fuels.",
        "tags": ["Green Hydrogen", "CO2 Capture", "Solar Fuels", "IISc Bangalore", "Catalysis"],
        "link": "https://www.linkedin.com/in/dr-laxman-gouda-49878337/",
        "badge": "Flagship Research"
    },
    {
        "id": 3,
        "title": "DESTINY — Marie Curie ITN Consortium",
        "subtitle": "EU Seventh Framework Programme (FP7)",
        "description": "Pan-European doctoral research across 9 perovskite groups in Europe/UK and 2 global PV companies. Focused on high-throughput combinatorial science and stability enhancement.",
        "tags": ["Marie Curie Fellow", "High-Throughput", "3GSolar", "Univ of Bath", "EU FP7"],
        "link": "https://www.linkedin.com/in/dr-laxman-gouda-49878337/",
        "badge": "EU Fellowship"
    },
    {
        "id": 4,
        "title": "Nanophotonics & Laser Interference Lithography",
        "subtitle": "Bar-Ilan Institute for Nanotechnology & Advanced Materials (BINA)",
        "description": "Ultra-low frequency Raman studies of hybrid perovskites, DBR microcavity-enhanced Raman signals with tunable cavity effect, and photonic structures via laser interference lithography.",
        "tags": ["BINA", "Nanophotonics", "Raman Spectroscopy", "Microcavity", "Lasing"],
        "link": "https://www.linkedin.com/in/dr-laxman-gouda-49878337/",
        "badge": "Optics & Photonics"
    }
]

# Working Prototypes Developed at ABX3PV (Equal 2x2 or 4x1 balanced grid)
PROTOTYPES = [
    {
        "title": "Perovskite Solar Cell Modules & Panels",
        "category": "Sheet-to-Sheet",
        "desc": "High-efficiency, scalable perovskite modules designed for rapid building integration and commercial rooftops."
    },
    {
        "title": "Flexible Perovskite Solar Cells",
        "category": "Roll-to-Roll",
        "desc": "Ultralight, flexible continuous roll substrates for portable electronics, IoT devices, and curved architectural surfaces."
    },
    {
        "title": "Silicon / Perovskite Tandem Solar Cells",
        "category": "High Efficiency",
        "desc": "Large-area tandem cells breaking theoretical single-junction silicon efficiency limits through dual-junction absorption."
    },
    {
        "title": "Perovskite Photovoltaics for Space",
        "category": "Extreme Environments",
        "desc": "Radiation-tolerant, high-power-to-weight ratio perovskite cells tailored for orbital satellites and space missions."
    }
]

EXPERIENCE = [
    {
        "role": "Co-Founder and CEO",
        "institution": "ABX3PV Private Limited",
        "affiliation": "Indian Institute of Science (IISc), Bangalore",
        "period": "2023 – Present",
        "description": "Leading deep-tech commercialization of next-generation Hybrid Perovskite solar cell modules. Pioneering industrial-scale sheet-to-sheet and continuous roll-to-roll manufacturing on rigid and flexible substrates."
    },
    {
        "role": "Ramanujan Fellow",
        "institution": "Indian Institute of Science (IISc)",
        "affiliation": "Bangalore Urban, Karnataka, India",
        "period": "April 2023 – Present",
        "description": "Developing industrial-scale manufacturing of Hybrid Perovskite solar cell modules. Spearheading photo-electrosynthesis of green Hydrogen and direct catalytic capture of CO2 converted into high-density fuels."
    },
    {
        "role": "Assistant Professor",
        "institution": "Indian Institute of Technology (IIT) Dharwad",
        "affiliation": "Dharwad, Karnataka, India",
        "period": "March 2023 – October 2023",
        "description": "Spearheaded research in renewable energy generation, energy storage devices, and clean-tech prototyping while mentoring engineering scholars."
    },
    {
        "role": "Postdoctoral Research Associate",
        "institution": "University of Pavia",
        "affiliation": "Pavia, Lombardy, Italy",
        "period": "November 2020 – March 2023",
        "description": "Conducted research on advanced perovskite formulations, interfacial defect engineering, and operational stability."
    },
    {
        "role": "Postdoctoral Research Scientist",
        "institution": "Universität Zürich & University of Jaume I",
        "affiliation": "Zurich, Switzerland & Spain",
        "period": "2018 – 2023",
        "description": "Specialized investigations into Artificial Photosynthesis, Solar fuel cells, and photoelectrochemical energy conversion."
    },
    {
        "role": "Postdoctoral Research Associate & Optics Specialist",
        "institution": "Bar-Ilan Institute for Nanotechnology (BINA)",
        "affiliation": "Bar-Ilan University, Israel",
        "period": "October 2017 – March 2023",
        "description": "Specialized in ultra-low frequency Raman spectroscopy of hybrid perovskites at room temperature, DBR microcavity-enhanced Raman signals with tunable cavity effect, laser interference lithography for nano-patterning, and lasing in hybrid perovskites."
    }
]

EDUCATION = [
    {
        "degree": "Ph.D., Hybrid Perovskite Organic-Inorganic Solar Cells / High-Throughput Study",
        "institution": "Bar-Ilan University, Israel",
        "period": "2014 – 2017",
        "details": "Funded by the EU ITN Marie Skłodowska-Curie Fellowship (DESTINY network). Worked across 9 leading European and UK research labs and 2 global photovoltaic companies. Focused on high-throughput fabrication, stability enhancement, and scalable deposition."
    },
    {
        "degree": "Junior Research Scientist (Thin Film Solar Cells)",
        "institution": "Indian Institute of Science (IISc), Bangalore",
        "period": "2012 – 2014",
        "details": "Conducted research on thin-film photovoltaic absorber layers, vacuum deposition technologies, and device characterization."
    },
    {
        "degree": "Master of Science (M.Sc.) in Inorganic Chemistry",
        "institution": "Karnatak University, Dharwad",
        "period": "2009 – 2011",
        "details": "Advanced studies in coordination chemistry, inorganic materials synthesis, and analytical spectroscopy."
    }
]

AREAS_OF_EXPERTISE = [
    {"name": "Hybrid Perovskite Solar Cells", "category": "Photovoltaics", "level": 98},
    {"name": "Roll-to-Roll & Flexible Substrates", "category": "Manufacturing", "level": 95},
    {"name": "Sheet-to-Sheet Module Fabrication", "category": "Scale-Up", "level": 94},
    {"name": "Silicon/Perovskite Tandem Cells", "category": "High Efficiency", "level": 92},
    {"name": "Space-Grade Perovskite PV", "category": "Extreme Environments", "level": 90},
    {"name": "Green Hydrogen Photo-Synthesis", "category": "Clean Energy", "level": 92},
    {"name": "Direct CO2 Capture & Solar Fuels", "category": "Decarbonization", "level": 90},
    {"name": "Raman Spectroscopy & Nano-Optics", "category": "Characterization", "level": 95},
]

@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        stats=STATS,
        slides=SLIDES,
        highlights=RECENT_HIGHLIGHTS,
        prototypes=PROTOTYPES,
        experience=EXPERIENCE,
        education=EDUCATION,
        skills=AREAS_OF_EXPERTISE,
        projects=PROJECTS,
    )

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please complete all required fields.", "error")
        return redirect(url_for("index") + "#contact")

    flash(f"Thank you, {name}! Your message has been sent to Dr. Laxman Gouda.", "success")
    return redirect(url_for("index") + "#contact")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
