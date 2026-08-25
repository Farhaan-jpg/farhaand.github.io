/**
 * Prepend NEXT_PUBLIC_BASE_PATH to any static asset path for GitHub Pages subpath hosting.
 */
export function withBasePath(path: string | null | undefined): string | null {
  if (!path) return null
  if (path.startsWith('http://') || path.startsWith('https://') || path.startsWith('data:')) {
    return path
  }
  const base = process.env.NEXT_PUBLIC_BASE_PATH || ''
  const cleanBase = base.replace(/\/+$/, '')
  const cleanPath = path.startsWith('/') ? path : `/${path}`
  return `${cleanBase}${cleanPath}`
}
