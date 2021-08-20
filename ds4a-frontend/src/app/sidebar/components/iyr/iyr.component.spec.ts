import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IyrComponent } from './iyr.component';

describe('IyrComponent', () => {
  let component: IyrComponent;
  let fixture: ComponentFixture<IyrComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ IyrComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(IyrComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
