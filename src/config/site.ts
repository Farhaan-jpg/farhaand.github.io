/**
 * ---------------------------------------------------------------------------
 * SITE CONTENT — FARHAAN D PORTFOLIO
 * ---------------------------------------------------------------------------
 * Personalized for Farhaan D according to the uploaded resume.
 * B.Sc. Computer Science with Cyber Security graduate and Aspiring Cybersecurity
 * & IT Professional.
 * ---------------------------------------------------------------------------
 */

export const site = {
  /** Shown letter-by-letter in the hero. Keep it short — it is the poster. */
  displayWord: 'PORTFOLIO',
  /** Index of the character in `displayWord` that the face illustration replaces. */
  faceLetterIndex: 5, // P-O-R-T-F-[O]-L-I-O

  eyebrow: 'CYBERSECURITY & IT PROFESSIONAL',
  year: '2026',

  firstName: 'FARHAAN',
  /**
   * The signature form the hero reveals as the visitor starts scrolling —
   * deliberately separate from `firstName`.
   */
  signatureName: 'FARHAAN D',
  lastName: 'D',

  /**
   * An invitation, not a job application. "Available to talk" rather than
   * "available for hire".
   */
  connect: {
    status: 'is available to talk',
    cta: "Let's connect",
    /** Points at the CONTACT section. */
    href: '#contact',
  },

  intro: {
    heading: 'HELLO',
    lede: "Hi, I'm FARHAAN.",
    paragraphs: [
      'I am a Computer Science graduate specializing in Cyber Security, networking, and system troubleshooting with hands-on experience in threat analysis, penetration testing, and secure system engineering.',
      "I've built automated security toolkits in Go, real-time threat detection Android applications with multi-engine scanning, and conducted hands-on vulnerability assessments during ethical hacking internships.",
      "Right now I'm focused on proactive defense, vulnerability research, network traffic analysis, and engineering secure, resilient digital infrastructure.",
    ],
  },

  education: {
    heading: 'EDUCATION',
    items: [
      {
        degree: 'B.Sc. Computer Science with Cyber Security',
        detail: 'Dr. N.G.P. Arts and Science College, Coimbatore | 2023 – 2026 (CGPA: 7.74/10 Distinction)',
      },
      {
        degree: 'Higher Secondary Certificate (12th Standard)',
        detail: 'Little Flower Convent Matric Hr. Sec. School, Tiruppur | 2022 – 2023 (82.17%)',
      },
      {
        degree: 'SSLC (10th Standard)',
        detail: 'Little Flower Convent Matric Hr. Sec. School, Tiruppur | 2020 – 2021',
      },
    ],
  },

  skills: {
    heading: 'SKILLS & TOOLS',
    /**
     * Farhaan's core cybersecurity & development stack.
     */
    items: [
      { label: 'Kali Linux', short: 'Kl', src: '/assets/skills/kali.png', scale: 1 },
      { label: 'Burp Suite', short: 'Bs', src: '/assets/skills/burp-suite.png', scale: 1 },
      { label: 'Wireshark', short: 'Ws', src: '/assets/skills/wireshark.png', scale: 1 },
      { label: 'Python', short: 'Py', src: '/assets/skills/python.svg', scale: 1 },
      { label: 'Go (Golang)', short: 'Go', src: '/assets/skills/go.svg', scale: 1 },
      { label: 'MySQL', short: 'My', src: '/assets/skills/mysql.png', scale: 1 },
    ] as { label: string; short: string; src: string | null; scale: number }[],
  },

  /**
   * PROJECTS & RESEARCH — Polaroid cards on physical paper.
   */
  studio: {
    heading: 'PROJECTS & RESEARCH',
    items: [
      {
        quote: "Smart QR Inspector — Enterprise Android app for real-time QR security threat detection (VirusTotal, Google Safe Browsing, URLhaus) & UPI scam defense.",
        author: 'Farhaan D · Android Security',
        rotation: -4,
        drop: 0,
        shade: 0.2,
        skew: -0.8,
        indent: 1,
        objectPosition: '50% 50%',
        href: null as string | null,
      },
      {
        quote: 'AutoBB — Automated Bug Bounty CLI toolkit in Go covering full recon, vulnerability scans (XSS, SQLi, SSRF, IDOR, CORS) & Nuclei integration.',
        author: 'Farhaan D · Security Automation',
        rotation: 1.2,
        drop: 11,
        shade: 0.6,
        skew: 0.7,
        indent: 0,
        objectPosition: '50% 50%',
        href: null as string | null,
      },
      {
        quote: 'Ethical Hacking & Network Traffic Analysis — Vulnerability scanning with Kali Linux, Wireshark packet inspection & TryHackMe Advent of Cyber.',
        author: 'Farhaan D · Threat Analysis',
        rotation: 3.5,
        drop: 3,
        shade: 0.35,
        skew: -0.5,
        indent: 2,
        objectPosition: '50% 50%',
        href: null as string | null,
      },
    ],
  },

  experience: {
    heading: 'EXPERIENCE & CERTIFICATIONS',
    items: [
      { period: 'May – Jun 2025', role: 'Cyber Security & Ethical Hacking Intern', company: 'Prompt Infotech, Coimbatore' },
      { period: '2024 – Present', role: 'Security Tool Developer & Researcher', company: 'Independent / Bug Bounty' },
      { period: 'Dec 2025', role: 'Advent of Cyber (24 Challenges)', company: 'TryHackMe' },
      { period: 'Dec 2025', role: 'Linux & Web Bug-Bounty Bootcamp', company: 'CappricioSec University' },
      { period: 'Jan 2025', role: 'Cybersecurity Workshop', company: 'ICCICT 2K25 (Curtin Univ, Malaysia & Dr. NGP)' },
      { period: 'Jan 2025', role: 'Cybersecurity Course', company: 'Tech Mahindra Foundation (NSDC)' },
    ],
  },

  /**
   * The last page. The giant heading IS the button.
   */
  footer: {
    heading: "Let's connect",
    acknowledged: 'Message sent',
    sub: 'Have a cybersecurity role, vulnerability inquiry, or security project in mind?',
    /** Farhaan's direct contact email */
    href: 'mailto:farhaandas4@gmail.com',
    marquee: ['FARHAAN', 'CYBERSECURITY', 'SECURITY RESEARCHER', 'ETHICAL HACKER'],
    links: [
      { label: 'LinkedIn', href: 'https://www.linkedin.com/in/farhaan-d-cybersecurity/' as string | null },
      { label: 'Email', href: 'mailto:farhaandas4@gmail.com' as string | null },
      { label: 'Phone', href: 'tel:+916369833215' as string | null },
    ],
  },
} as const

export type Site = typeof site


