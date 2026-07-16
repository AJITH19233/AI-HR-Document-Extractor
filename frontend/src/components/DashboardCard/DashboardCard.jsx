import {
  Card,
  CardContent,
  Typography,
  Box,
} from "@mui/material";

import TrendingUpIcon from "@mui/icons-material/TrendingUp";

import "./DashboardCard.css";

function DashboardCard({

    title,

    value,

    icon,

    color,

    subtitle="Updated just now"

}){

    return(

        <Card className="dashboard-card">

            <CardContent>

                <Box
                    className="card-top"
                >

                    <Box
                        className="card-icon"
                        sx={{
                            background:color
                        }}
                    >

                        {icon}

                    </Box>

                    <TrendingUpIcon
                        sx={{
                            color:"#22C55E"
                        }}
                    />

                </Box>

                <Typography
                    className="card-title"
                >

                    {title}

                </Typography>

                <Typography
                    className="card-value"
                >

                    {value}

                </Typography>

                <Typography
                    className="card-subtitle"
                >

                    {subtitle}

                </Typography>

            </CardContent>

        </Card>

    );

}

export default DashboardCard;