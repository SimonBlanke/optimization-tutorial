# Optimization Tutorial - Svelte Implementation

A modern, interactive web application for learning gradient-free optimization algorithms. Built with SvelteKit for optimal performance and user experience.

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Node.js** (version 18.0 or higher)
- **npm** (comes with Node.js) or **yarn**
- **Git** (for cloning the repository)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd optimization-tutorial/svelte-optimization-tutorial
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```
   
   Or if you prefer yarn:
   ```bash
   yarn install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```
   
   Or with yarn:
   ```bash
   yarn dev
   ```

4. **Open in browser**
   
   Navigate to `http://localhost:5173` in your web browser. The application will automatically reload when you make changes to the code.

## 📋 Detailed Setup Guide

### Installing Node.js

#### Windows
1. Visit [nodejs.org](https://nodejs.org/)
2. Download the LTS version (recommended)
3. Run the installer and follow the installation wizard
4. Verify installation by opening Command Prompt and running:
   ```bash
   node --version
   npm --version
   ```

#### macOS
**Option 1: Direct Download**
1. Visit [nodejs.org](https://nodejs.org/)
2. Download the LTS version
3. Run the installer

**Option 2: Using Homebrew**
```bash
brew install node
```

#### Linux (Ubuntu/Debian)
```bash
# Update package index
sudo apt update

# Install Node.js
sudo apt install nodejs npm

# Verify installation
node --version
npm --version
```

#### Linux (CentOS/RHEL)
```bash
# Install Node.js using NodeSource repository
curl -fsSL https://rpm.nodesource.com/setup_lts.x | sudo bash -
sudo yum install nodejs npm
```

### Verifying Your Installation

After installing Node.js and npm, verify they're working correctly:

```bash
node --version  # Should show v18.x.x or higher
npm --version   # Should show 8.x.x or higher
```

### Project Structure

```
svelte-optimization-tutorial/
├── src/
│   ├── lib/
│   │   ├── components/          # Reusable Svelte components
│   │   │   ├── Sidebar.svelte
│   │   │   ├── ParameterControl.svelte
│   │   │   └── VisualizationPanel.svelte
│   │   ├── data/               # Algorithm data and configurations
│   │   └── utils/              # Utility functions
│   ├── routes/
│   │   ├── +layout.svelte      # Main layout component
│   │   ├── +page.svelte        # Landing page
│   │   ├── overview/           # Algorithm overview page
│   │   └── optimizers/         # Individual optimizer pages
│   │       └── hill-climbing/  # Example optimizer page
│   └── app.html                # HTML template
├── static/                     # Static assets (images, GIFs, etc.)
├── package.json                # Dependencies and scripts
├── svelte.config.js           # Svelte configuration
└── vite.config.js             # Vite build configuration
```

## 🛠️ Development Guide

### Available Scripts

- **`npm run dev`** - Start development server with hot reload
- **`npm run build`** - Build the application for production
- **`npm run preview`** - Preview the production build locally
- **`npm run check`** - Run Svelte type checking
- **`npm run check:watch`** - Run type checking in watch mode

### Adding New Optimization Algorithms

1. **Create a new route directory**
   ```bash
   mkdir src/routes/optimizers/your-algorithm-name
   ```

2. **Create the page component**
   ```bash
   touch src/routes/optimizers/your-algorithm-name/+page.svelte
   ```

3. **Use the existing template structure**
   - Copy the structure from `src/routes/optimizers/hill-climbing/+page.svelte`
   - Update the algorithm information, parameters, and descriptions
   - Add algorithm-specific visualizations

4. **Update the sidebar navigation**
   - Edit `src/lib/components/Sidebar.svelte`
   - Add your algorithm to the appropriate category in the `optimizers` array

5. **Add to overview page**
   - Edit `src/routes/overview/+page.svelte`
   - Add your algorithm to the `optimizers` array with scoring information

### Working with Assets

1. **Static assets** (images, GIFs, etc.) go in the `static/` directory
2. **Reference assets** in your components using absolute paths: `/assets/algorithm-name/visualization.gif`
3. **Organize assets** by algorithm in subfolders: `static/assets/hill-climbing/`

### Styling Guidelines

- Use **CSS custom properties** for consistent theming
- Follow **mobile-first** responsive design principles
- Use **semantic HTML** elements for accessibility
- Maintain **consistent spacing** using rem units
- Use **descriptive class names** following BEM methodology when appropriate

## 🎨 Customization

### Theming

The application uses CSS custom properties for theming. Key colors can be modified in the root CSS:

```css
:root {
  --primary-color: #3b82f6;
  --secondary-color: #64748b;
  --success-color: #059669;
  --warning-color: #dc2626;
  --background-color: #f8fafc;
  --text-color: #334155;
}
```

### Adding Custom Components

1. Create your component in `src/lib/components/`
2. Export it from the component file
3. Import and use in your pages:
   ```svelte
   <script>
     import MyComponent from '$lib/components/MyComponent.svelte';
   </script>
   ```

## 🚢 Deployment

### Building for Production

```bash
npm run build
```

This creates a `build` directory with the compiled application.

### Deployment Options

#### Vercel (Recommended)
1. Push your code to a Git repository
2. Connect your repository to Vercel
3. Vercel will automatically deploy on every push

#### Netlify
1. Build the project: `npm run build`
2. Upload the `build` directory to Netlify
3. Configure redirects for SPA routing

#### Static Hosting
The built application is a static site and can be hosted on any static hosting service:
- GitHub Pages
- Amazon S3 + CloudFront
- Google Firebase Hosting

### Environment Variables

Create a `.env` file in the root directory for environment-specific configuration:

```
VITE_API_URL=your-api-url
VITE_ANALYTICS_ID=your-analytics-id
```

Access in your components with:
```javascript
import { env } from '$env/dynamic/public';
const apiUrl = env.VITE_API_URL;
```

## 🔧 Troubleshooting

### Common Issues

**1. Port already in use**
```bash
# Kill process using port 5173
sudo lsof -ti:5173 | xargs sudo kill -9

# Or start on a different port
npm run dev -- --port 3000
```

**2. Module resolution errors**
- Clear node_modules and reinstall:
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  ```

**3. Build failures**
- Check for TypeScript errors: `npm run check`
- Ensure all imports use correct paths with `$lib` alias

**4. Assets not loading**
- Verify assets are in the `static/` directory
- Use absolute paths starting with `/`
- Check browser network tab for 404 errors

### Performance Tips

1. **Lazy load images** with the `loading="lazy"` attribute
2. **Optimize GIFs** - consider converting to WebP or MP4
3. **Code splitting** - SvelteKit handles this automatically
4. **Preload critical resources** in `app.html`

### Development Best Practices

1. **Use TypeScript** for better development experience
2. **Write tests** for components using @testing-library/svelte
3. **Follow accessibility guidelines** (WCAG 2.1)
4. **Optimize for SEO** with proper meta tags and structured data
5. **Monitor performance** with Lighthouse audits

## 📚 Learning Resources

### SvelteKit Documentation
- [Official SvelteKit Docs](https://kit.svelte.dev/)
- [Svelte Tutorial](https://svelte.dev/tutorial)

### Optimization Algorithm Resources
- [Gradient-Free-Optimizers Documentation](https://github.com/SimonBlanke/Gradient-Free-Optimizers)
- [Original Tutorial Repository](https://github.com/SimonBlanke/optimization-tutorial)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes and test thoroughly
4. Commit with descriptive messages
5. Push to your fork: `git push origin feature/your-feature-name`
6. Create a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ✨ Next Steps

Once you have the application running:

1. **Explore the landing page** to understand the tutorial structure
2. **Check out the overview page** to see algorithm comparisons
3. **Visit individual algorithm pages** to see the interactive parameter controls
4. **Add your own algorithms** using the hill-climbing page as a template
5. **Integrate existing assets** from the original optimization-tutorial repository

The application is designed to be easily extensible - you can add new algorithms, visualizations, and interactive features by following the established patterns in the codebase.