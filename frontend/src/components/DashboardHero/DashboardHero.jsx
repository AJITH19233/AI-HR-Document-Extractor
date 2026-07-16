import {
  Box,
  Typography,
  Button,
} from "@mui/material";

import UploadFileIcon from "@mui/icons-material/UploadFile";
import AutoAwesomeIcon from "@mui/icons-material/AutoAwesome";

import "./DashboardHero.css";

function DashboardHero() {

    const hour = new Date().getHours();

    let greeting = "Good Evening";

    if(hour < 12){
        greeting = "Good Morning";
    }
    else if(hour < 18){
        greeting = "Good Afternoon";
    }

    return (

        <Box className="hero">

            <Box>

                <Typography
                    variant="h4"
                    fontWeight="700"
                >
                    {greeting}, Ajith 👋
                </Typography>

                <Typography
                    className="hero-subtitle"
                >
                    Welcome to your AI-powered recruitment dashboard.
                    Track resumes, analyze candidates, and streamline hiring.
                </Typography>

            </Box>

            <Box
                sx={{
                    display:"flex",
                    gap:2
                }}
            >

                <Button
                    variant="contained"
                    startIcon={<UploadFileIcon/>}
                    size="large"
                >
                    Upload Resume
                </Button>
<Button
    variant="contained"
    color="warning"
    startIcon={<AutoAwesomeIcon />}
    size="large"
>
    AI Analysis
</Button>

            </Box>

        </Box>

    );

}

export default DashboardHero;