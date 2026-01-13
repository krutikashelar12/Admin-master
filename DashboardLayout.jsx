import { useNavigate, useLocation, Outlet } from "react-router-dom";
import {
  FaHome,
  FaBuilding,
  FaThLarge,
  FaBox,
  FaFileAlt,
  FaDatabase,
  FaFile,
} from "react-icons/fa";

export default function DashboardLayout() {
  const navigate = useNavigate();
  const location = useLocation();

  const menuItems = [
    { name: "Dashboard", path: "/", icon: <FaHome /> },
    { name: "Tenants", path: "/tenant", icon: <FaBuilding /> },
    { name: "Applications", path: "/application", icon: <FaThLarge /> },
    { name: "Products", path: "/product", icon: <FaBox /> },
    { name: "Contents", path: "/content", icon: <FaFileAlt /> },
    { name: "CD Master", path: "/cd-master", icon: <FaDatabase /> },
    { name: "Templates", path: "/template", icon: <FaFile /> },
  ];

  return (
    <div style={{ display: "flex", minHeight: "100vh" }}>
      {/* ===== SIDEBAR ===== */}
      <aside
        style={{
          width: 260,
          background: "linear-gradient(180deg, #312e81, #4338ca)",
          color: "#fff",
          padding: "30px 20px",
          display: "flex",
          flexDirection: "column",
        }}
      >
        <h2 style={{ marginBottom: 30 }}>Bank Admin</h2>

        <ul style={{ listStyle: "none", padding: 0, flex: 1 }}>
          {menuItems.map((item) => {
            const active = location.pathname === item.path;
            return (
              <li
                key={item.name}
                onClick={() => navigate(item.path)}
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 12,
                  padding: "12px 16px",
                  marginBottom: 10,
                  cursor: "pointer",
                  borderRadius: 6,
                  background: active
                    ? "rgba(255,255,255,0.15)"
                    : "transparent",
                  borderLeft: active
                    ? "4px solid #facc15"
                    : "4px solid transparent",
                }}
              >
                {item.icon}
                {item.name}
              </li>
            );
          })}
        </ul>

        <button
          onClick={() => navigate("/login")}
          style={{
            background: "red",
            color: "#fff",
            padding: 12,
            border: "none",
            borderRadius: 6,
            cursor: "pointer",
          }}
        >
          Logout
        </button>
      </aside>

      {/* ===== RIGHT CONTENT (IMPORTANT) ===== */}
      <main
        style={{
          flex: 1,
          padding: 30,
          background: "#f5f7fb",
          overflowY: "auto",
        }}
      >
        {/* 👇👇 THIS WAS MISSING 👇👇 */}
        <Outlet />
      </main>
    </div>
  );
}
