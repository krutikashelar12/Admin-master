import React from "react";
import { NavLink } from "react-router-dom";
import "../styles/sidebar.css";


export default function Sidebar() {
  const menuItems = [
    { name: "Tenant", path: "/tenant" },
    { name: "Application", path: "/application" },
    { name: "Product", path: "/product" },
    { name: "Content", path: "/content" },
    { name: "CD", path: "/cd" },
    { name: "Template", path: "/template" },
  ];

  return (
    <aside className="sidebar">
      <h2 className="sidebar-logo">MDM System</h2>
      <ul className="sidebar-menu">
        {menuItems.map((item) => (
          <li key={item.name}>
            <NavLink
              to={item.path}
              className={({ isActive }) =>
                isActive ? "active-link" : "inactive-link"
              }
            >
              {item.name}
            </NavLink>
          </li>
        ))}
      </ul>
    </aside>
  );
}
