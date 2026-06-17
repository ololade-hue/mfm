from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# Create PDF
pdf_file = 'services.pdf'
doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
styles = getSampleStyleSheet()
story = []

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor='purple',
    spaceAfter=12,
    alignment=TA_CENTER
)

service_title_style = ParagraphStyle(
    'ServiceTitle',
    parent=styles['Heading2'],
    fontSize=14,
    textColor='#c91e63',
    spaceAfter=6,
    spaceBefore=6
)

# Title
story.append(Paragraph('MOUNTAIN OF FIRE AND MIRACLE MINISTRY', title_style))
story.append(Paragraph('Our Services', styles['Heading1']))
story.append(Spacer(1, 0.3*inch))

# Services
services = [
    ('Power Must Change Hands', 'Spiritual warfare prayer session to break the chains of oppression and claim victory over the enemy. Experience divine authority and reclaim your spiritual power.'),
    ('Manna Water', 'Divine sustenance for your spirit. This anointed service provides spiritual nourishment and breakthrough blessings for all areas of your life.'),
    ('Prayer Rain', 'Intensive intercession sessions where prayers descend like rain for healing, deliverance, and divine intervention in your circumstances.'),
    ('Deliverance Sessions', 'Comprehensive spiritual deliverance from bondage, demonic oppression, and spiritual attacks. Experience freedom and wholeness in Christ.'),
    ('Night Vigils', 'All-night prayer services for intense intercession, worship, and fellowship with God. Seek His face and receive supernatural encounters.'),
    ('Anointing & Laying on of Hands', 'Receive the power of the Holy Spirit through prayer and anointing oil. Experience divine healing, transformation, and supernatural empowerment.')
]

for service_title, service_desc in services:
    story.append(Paragraph(f'<b>{service_title}</b>', service_title_style))
    story.append(Paragraph(service_desc, styles['BodyText']))
    story.append(Spacer(1, 0.15*inch))

# Social Media Section
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph('Connect With Us', styles['Heading1']))
story.append(Paragraph('Follow our ministry on social media for daily spiritual content and updates:', styles['Normal']))
story.append(Spacer(1, 0.15*inch))

socials = [
    '<b>YouTube:</b> https://www.youtube.com/c/mountainoffireandmiracles',
    '<b>Instagram:</b> https://www.instagram.com/mountainoffireandmiracles',
    '<b>Facebook:</b> https://www.facebook.com/mountainoffireandmiracles',
    '<b>Spotify:</b> https://open.spotify.com/artist/mountainoffireandmiracles'
]

for social in socials:
    story.append(Paragraph(social, styles['Normal']))
    story.append(Spacer(1, 0.1*inch))

# Footer
story.append(Spacer(1, 0.4*inch))
footer_style = ParagraphStyle('Footer', parent=styles['Normal'], fontSize=10, textColor='#666666', alignment=TA_CENTER)
story.append(Paragraph('&copy; 2026 Mountain of Fire and Miracle Ministry<br/>Spirit-filled Deliverance Ministry', footer_style))

# Build PDF
doc.build(story)
print(f'PDF created successfully: {pdf_file}')
