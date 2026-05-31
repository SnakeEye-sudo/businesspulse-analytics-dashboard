# BusinessPulse Analytics Dashboard

![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue?logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-38bdf8?logo=tailwindcss)
![Recharts](https://img.shields.io/badge/Recharts-2.x-ff6b6b)
![License](https://img.shields.io/badge/License-MIT-green)

A modern, production-ready **Business Analytics Dashboard** built with Next.js 15, TypeScript, and Tailwind CSS. Real-time KPI tracking, interactive charts, and AI-ready data pipeline.

![Dashboard Preview](https://via.placeholder.com/1200x600/0f172a/38bdf8?text=BusinessPulse+Analytics+Dashboard)

## Features

- **KPI Cards** — Revenue, Users, Orders, Conversion Rate with trend indicators
- **Revenue Chart** — Monthly bar/line chart with Recharts
- **Sales Funnel** — Visualize lead-to-customer conversion
- **Top Products Table** — Sortable, filterable product performance table
- **Geographic Heatmap** — Regional sales distribution
- **Dark/Light Mode** — System-aware theme toggle
- **Responsive Layout** — Mobile-first sidebar with collapsible navigation
- **Mock Data API** — JSON-based data layer, easy to swap with real backend
- **TypeScript** — Fully typed components and data models

## Tech Stack

| Layer | Technology |
|-------|------------|
| Framework | Next.js 15 (App Router) |
| Language | TypeScript 5 |
| Styling | Tailwind CSS 3.4 |
| Charts | Recharts 2.x |
| Icons | Lucide React |
| State | React Context + useReducer |
| Data | Mock JSON API (ready for REST/GraphQL) |
| Deployment | Vercel |

## Project Structure

```
businesspulse-analytics-dashboard/
├── src/
│   ├── app/
│   │   ├── layout.tsx          # Root layout with sidebar
│   │   ├── page.tsx            # Main dashboard page
│   │   ├── globals.css         # Global styles
│   │   └── api/
│   │       └── metrics/
│   │           └── route.ts    # Mock metrics API endpoint
│   ├── components/
│   │   ├── dashboard/
│   │   │   ├── KPICard.tsx     # Key Performance Indicator card
│   │   │   ├── RevenueChart.tsx # Monthly revenue bar chart
│   │   │   ├── SalesFunnel.tsx  # Funnel chart component
│   │   │   └── TopProducts.tsx  # Products performance table
│   │   ├── layout/
│   │   │   ├── Sidebar.tsx     # Collapsible navigation sidebar
│   │   │   ├── Header.tsx      # Top header with search & profile
│   │   │   └── ThemeToggle.tsx # Dark/light mode toggle
│   │   └── ui/
│   │       ├── Badge.tsx       # Status badge component
│   │       ├── Card.tsx        # Reusable card wrapper
│   │       └── Spinner.tsx     # Loading spinner
│   ├── data/
│   │   └── mockData.ts         # Mock business metrics data
│   ├── hooks/
│   │   ├── useMetrics.ts       # Data fetching hook
│   │   └── useTheme.ts         # Theme management hook
│   └── types/
│       └── index.ts            # TypeScript type definitions
├── public/
│   └── favicon.ico
├── package.json
├── tailwind.config.ts
├── tsconfig.json
├── next.config.ts
└── README.md
```

## Getting Started

### Prerequisites

- Node.js 18+
- npm / yarn / pnpm

### Installation

```bash
# Clone the repository
git clone https://github.com/SnakeEye-sudo/businesspulse-analytics-dashboard.git
cd businesspulse-analytics-dashboard

# Install dependencies
npm install

# Run development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build for Production

```bash
npm run build
npm start
```

### Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/SnakeEye-sudo/businesspulse-analytics-dashboard)

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/metrics` | All dashboard KPIs |
| `GET` | `/api/metrics?type=revenue` | Monthly revenue data |
| `GET` | `/api/metrics?type=products` | Top products data |
| `GET` | `/api/metrics?type=funnel` | Sales funnel data |

## Screenshots

| Section | Preview |
|---------|--------|
| KPI Overview | Revenue, Users, Orders, Conversion |
| Revenue Chart | Monthly trend with comparison |
| Products Table | Top 10 products with filters |

## Contributing

Pull requests are welcome! Please open an issue first to discuss major changes.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'feat: add amazing feature'`
4. Push: `git push origin feature/amazing-feature`
5. Open a Pull Request

## Author

**Er. Sangam Krishna** — [@SnakeEye-sudo](https://github.com/SnakeEye-sudo)

Web App Developer & Data Analyst | Open to full-time roles & freelance

## License

MIT License — see [LICENSE](LICENSE) for details.
