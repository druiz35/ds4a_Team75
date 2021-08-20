import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SidebarRoutingModule } from './sidebar-routing.module';
import { WrapperComponent } from './components/wrapper/wrapper.component';
import { AboutComponent } from './components/about/about.component';
import { DataDashboardComponent } from './components/data-dashboard/data-dashboard.component';
import { ModelsComponent } from './components/models/models.component';
import { IyrComponent } from './components/iyr/iyr.component';
import { MatSidenavModule } from "@angular/material/sidenav";
import { MatIconModule } from "@angular/material/icon";
import { MatListModule } from "@angular/material/list";
import { MatToolbarModule } from "@angular/material/toolbar";

@NgModule({
  declarations: [
    WrapperComponent,
    AboutComponent,
    DataDashboardComponent,
    ModelsComponent,
    IyrComponent
  ],
  imports: [
    CommonModule,
    SidebarRoutingModule,
    MatSidenavModule,
    MatIconModule,
    MatListModule,
    MatToolbarModule
  ]
})
export class SidebarModule { }
