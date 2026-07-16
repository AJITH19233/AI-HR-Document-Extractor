import {
  AppBar,
  Toolbar,
  Typography,
  Box,
  Avatar,
  Badge,
  IconButton,
  InputBase,
  Paper
} from "@mui/material";

import SearchIcon from "@mui/icons-material/Search";
import NotificationsNoneIcon from "@mui/icons-material/NotificationsNone";
import DarkModeOutlinedIcon from "@mui/icons-material/DarkModeOutlined";
import SettingsOutlinedIcon from "@mui/icons-material/SettingsOutlined";

import "./Navbar.css";

function Navbar() {

    const today = new Date();

    return (

        <AppBar
            position="sticky"
            elevation={0}
            className="navbar"
        >

            <Toolbar>

                <Box
                    sx={{
                        flexGrow:1
                    }}
                >

                    <Typography
                        variant="h4"
                    >


                    </Typography>

                    <Typography
                        color="text.secondary"
                    >

                        {today.toDateString()}

                    </Typography>

                </Box>

                <Paper
                    className="search-box"
                >

                    <SearchIcon
                        sx={{
                            color:"#94A3B8"
                        }}
                    />

                    <InputBase
                        placeholder="Search candidates..."
                        sx={{
                            ml:1,
                            flex:1
                        }}
                    />

                </Paper>

                <IconButton>

                    <Badge
                        badgeContent={4}
                        color="error"
                    >

                        <NotificationsNoneIcon/>

                    </Badge>

                </IconButton>

                <IconButton>

                    <DarkModeOutlinedIcon/>

                </IconButton>

                <IconButton>

                    <SettingsOutlinedIcon/>

                </IconButton>

                <Avatar
                    sx={{
                        ml:2,
                        bgcolor:"#2563EB",
                        width:45,
                        height:45
                    }}
                >

                    A

                </Avatar>

            </Toolbar>

        </AppBar>
    );
}
export default Navbar;