let basePath = process.env.NEXT_PUBLIC_BASE_PATH || '';
if (!basePath && process.env.GITHUB_REPOSITORY) {
  const repo = process.env.GITHUB_REPOSITORY.split('/')[1];
  basePath = `/${repo}`;
}
basePath = basePath.replace(/\/+$/, '');

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  devIndicators: false,
  output: 'export',
  basePath: basePath || undefined,
  assetPrefix: basePath ? `${basePath}/` : undefined,
  env: {
    NEXT_PUBLIC_BASE_PATH: basePath,
  },
  images: {
    unoptimized: true,
    formats: ['image/avif', 'image/webp'],
  },
}

export default nextConfig
