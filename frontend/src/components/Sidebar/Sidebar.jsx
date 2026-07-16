import {
  Dashboard,
  Description,
  Search,
  FilterAlt,
  Analytics,
  ChevronLeft,
} from "@mui/icons-material";

import {
  Box,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Typography,
  IconButton,
} from "@mui/material";

import { useState } from "react";

import "./Sidebar.css";

const menuItems = [
  {
    text: "Dashboard",
    icon: <Dashboard />,
  },
  {
    text: "Resumes",
    icon: <Description />,
  },
  {
    text: "Search",
    icon: <Search />,
  },
  {
    text: "Filters",
    icon: <FilterAlt />,
  },
  {
    text: "Analytics",
    icon: <Analytics />,
  },
];

function Sidebar() {
  const [active, setActive] = useState("Dashboard");

  return (
    <Box
      className="sidebar"
    >
      <Box className="sidebar-header">

        <Typography
          variant="h5"
          fontWeight="700"
        >
          AI HR ATS
        </Typography>

        <IconButton
          sx={{
            color: "white",
          }}
        >
          <ChevronLeft />
        </IconButton>

      </Box>

      <Typography
        className="sidebar-subtitle"
      >
        Recruiter Portal
      </Typography>

      <List
        sx={{
          mt: 4,
        }}
      >
        {menuItems.map((item) => (

          <ListItemButton
            key={item.text}
            className={
              active === item.text
                ? "active-menu"
                : "menu-item"
            }
            onClick={() => setActive(item.text)}
          >

            <ListItemIcon
    sx={{
        color:"inherit",

        "& svg":{

            fontSize:26

        }

    }}
></ListItemIcon>

            <ListItemText
              primary={item.text}
            />

          </ListItemButton>

        ))}
      </List>

      <Box className="sidebar-footer">

        <Typography
          variant="body2"
        >
          HR Document Extractor
        </Typography>

        <Typography
          variant="caption"
        >
          Version 2.0
        </Typography>

      </Box>

    </Box>
  );
}

export default Sidebar;