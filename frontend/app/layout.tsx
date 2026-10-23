import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Math AI Assistant",
  description: "Assistant IA pour résoudre des problèmes mathématiques",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr">
      <body>{children}</body>
    </html>
  );
}
